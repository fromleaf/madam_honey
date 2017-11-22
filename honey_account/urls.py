#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from .routers import account_router
from .views import SignUpView

urlpatterns = [
    url(r'^', include(account_router.urls)),
    url(r'^sign_up/$', SignUpView.as_view(), name='sign_up'),
    # url(r'^sign-in', include(SignInViewSet, namespace='sign-in')),
    # url(r'^sign-out', include(SignOutViewSet, namespace='sign-out')),
]