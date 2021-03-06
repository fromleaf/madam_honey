#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.urls import reverse


class ChatRoom(models.Model):
    name = models.TextField()
    label = models.SlugField(
        unique=True,
        help_text='This label will be automatically made by Haikunator Library.'
    )

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('honey-chat:chatroom', args=[self.label])


class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    def __unicode__(self):
        return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')

    def as_dict(self):
        return {
            'handle': self.handle, 'message': self.message,
            'timestamp': self.formatted_timestamp
        }
