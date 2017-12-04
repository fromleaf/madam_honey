#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from rest_framework import routers

from .viewsets import UserViewSet, GroupViewSet


# For API
users_routers = routers.DefaultRouter()
users_routers.register(r'users', UserViewSet)
users_routers.register(r'groups', GroupViewSet)

urlpatterns = [
    url(
        r'', include(users_routers.urls, namespace='users-api')
    ),
]
