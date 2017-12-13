#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import (ThanksView, SignupView, LoginView, LogoutView)


urlpatterns = [
    # For normal page
    url(r'signup/$', SignupView.as_view(), name='signup'),
    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'logout/$', LogoutView.as_view(), name='logout'),
    url(r'thanks/$', ThanksView.as_view(), name='thanks'),
]
