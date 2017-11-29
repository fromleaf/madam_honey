#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from .routers import account_router
from .views import (
    ThanksView, SignUpView, LogInView,
    SignUpAPIView
)

urlpatterns = [
    url(r'', include(account_router.urls)),
    # For normal page
    url(r'^sign-up/$', SignUpView.as_view(), name='sign-up'),
    url(r'^log-in/$', LogInView.as_view(), name='log-in'),
    url(r'^thanks/$', ThanksView.as_view(), name='thanks'),

    # For API
    url(
        r'^(?P<version>(v1|v2))/sign-up/$',
        SignUpAPIView.as_view(), name='api-sign-up'
    ),
    # url(r'^sign-in', include(SignInViewSet, namespace='sign-in')),
    # url(r'^sign-out', include(SignOutViewSet, namespace='sign-out')),
]