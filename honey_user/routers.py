#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import routers

from .viewsets import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
