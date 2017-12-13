#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from haikunator import Haikunator

from .models import ChatRoom


class ChatRoomMainView(TemplateView):
    template_name = 'honey_chat/main.html'

    def post(self, request, *args, **kwargs):
        haikunator = Haikunator()
        label = haikunator.haikunate()
        chatroom, created = ChatRoom.objects.get_or_create(label=label)
        return redirect(chatroom)


class ChatRoomView(DetailView):
    template_name = 'honey_chat/chatroom.html'
    model = ChatRoom
    slug_field = 'label'

    def get(self, request, *args, **kwargs):
        return super(ChatRoomView, self).get(self, request, *args, **kwargs)
