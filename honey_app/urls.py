#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import HoneyAppMainView

urlpatterns = [
    url(r'^main/$', HoneyAppMainView.as_view(), name='honey-app-main'),
]
