#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import routers

from .viewsets import UserViewSet, GroupViewSet


account_routers = routers.DefaultRouter()
account_routers.register(r'(?P<version>(v1|v2))/users', UserViewSet)
account_routers.register(r'(?P<version>(v1|v2))/groups', GroupViewSet)
