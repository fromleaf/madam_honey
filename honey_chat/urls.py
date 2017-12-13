#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import (
    ChatRoomMainView, ChatRoomView
)

urlpatterns = [
    url(r'^$', ChatRoomMainView.as_view(), name='main'),
    url(r'(?P<slug>[\w-]+)/$', ChatRoomView.as_view(), name='chatroom'),
]
