#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from .viewsets import (
    SignUpViewSet, SignInViewSet, SignOutViewSet
)

urlpatterns = [
    url(r'^sign-up', include(SignUpViewSet, namespace='sign-up')),
    url(r'^sign-in', include(SignInViewSet, namespace='sign-in')),
    url(r'^sign-out', include(SignOutViewSet, namespace='sign-out')),
]