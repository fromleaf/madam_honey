#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import routers

from .viewsets import UserViewSet, GroupViewSet


account_router = routers.DefaultRouter()
account_router.register(r'users', UserViewSet)
account_router.register(r'groups', GroupViewSet)
