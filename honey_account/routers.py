#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from rest_framework import routers

from .viewsets import (
    AccountViewSet, CreateAccountViewSet
)


# For API
account_routers = routers.DefaultRouter()
account_routers.register(r'create', CreateAccountViewSet)
account_routers.register(r'', AccountViewSet)


urlpatterns = [
    url(r'', include(account_routers.urls, namespace='account-api')),
]
