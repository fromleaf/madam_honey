#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import json
import logging

from django.http import HttpResponse

from channels import Channel, Group
from channels.sessions import channel_session
from channels.handler import AsgiHandler
from channels.auth import (
    http_session_user, channel_session_user, channel_session_user_from_http
)

from .models import ChatRoom, Message

log = logging.getLogger(__name__)


@channel_session
def ws_connect(message):
    try:
        path = message.content['path'].strip('/').split('/')
        prefix = path[0]
        label = path[2]
        if prefix != 'chat':
            log.debug('invalid ws path={}'.format(message.content['path']))
            return

        chatroom = ChatRoom.objects.get(label=label)
    except ValueError:
        log.debug('invalid ws path={}'.format(message.content['path']))
        return

    except ChatRoom.DoesNotExist:
        log .debug('ws room does not exist label={}'.format(label))
        return

    log.debug('chat connect room={} client={}:{} path={} reply_channel={}'.format(
        chatroom.label, message.content['client'][0], message.content['client'][1],
        message.content['path'], message.reply_channel
    ))

    message.reply_channel.send({"accept": True})
    Group(
        'chat-' + label, channel_layer=message.channel_layer
    ).add(message.reply_channel)

    message.channel_session['chatroom'] = chatroom.label


@channel_session
def ws_receive(message):
    try:
        label = message.channel_session['chatroom']
        chatroom = ChatRoom.objects.get(label=label)
        log.debug('recieved message, chatroom exist label={}'.format(
            chatroom.label
        ))

    except KeyError:
        log.debug('no room in channel_session')
        return

    except ChatRoom.DoesNotExist:
        log.debug('recieved message, buy chatroom does not exist label={}'.format(
            label
        ))
        return

    try:
        data = json.loads(message['text'])
    except ValueError:
        log.debug("ws message isn't json text")
        return

    if set(data.keys()) != {'handle', 'message'}:
        log.debug("ws message unexpected from data={}".format(data))
        return

    if data:
        log.debug('chat message room={} handle={} message={}'.format(
            chatroom.label, data['handle'], data['message']
        ))
        m = chatroom.messages.create(**data)

        Group('chat-'+label, channel_layer=message.channel_layer).send(
            {'text': json.dumps(m.as_dict())}
        )


@channel_session
def ws_disconnect(message):
    try:
        label = message.channel_session['room']
        chatroom = ChatRoom.objects.get(label=label)
        Group('chat-'+label, channel_layer=message.channel_layer).discard(
            message.reply_channel
        )
    except (KeyError, ChatRoom.DoesNotExist):
        pass
