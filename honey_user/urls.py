#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .routers import UserViewSet

user_router = DefaultRouter()
user_router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(user_router.urls)),
]
