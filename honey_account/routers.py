#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from rest_framework import routers

from .viewsets import (
    AccountViewSet, SignUpViewSet, SignUpWithOAuth2ViewSet
)

# For API
account_routers = routers.DefaultRouter()
account_routers.register(r'users', AccountViewSet)

sign_routers = routers.DefaultRouter()
sign_routers.register(r'signup', SignUpViewSet)
sign_routers.register(r'signup-oauth2', SignUpWithOAuth2ViewSet)

urlpatterns = [
    url(r'', include(account_routers.urls, namespace='account-api')),
    url(r'', include(sign_routers.urls, namespace='sign-api')),
]
