#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from honey_common.viewsets import CUViewSet, RDViewSet
from .serializers import (
    AccountSerializer, CreateAccountSerializer,
    AccountWithJWTSerializer, CreateAccountWithJWTSerializer
)


class AccountViewSet(RDViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all().order_by('id')
    serializer_class = AccountSerializer


class SignUpViewSet(CUViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all().order_by('id')
    serializer_class = CreateAccountSerializer

    def create(self, request, *args, **kwargs):
        return super(SignUpViewSet, self).create(request, *args, **kwargs)


class AccountWithJWTViewSet(RDViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all().order_by('id')
    serializer_class = AccountWithJWTSerializer


class SignUpWithJWTViewSet(CUViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all().order_by('id')
    serializer_class = CreateAccountWithJWTSerializer

    def create(self, request, *args, **kwargs):
        return super(SignUpWithJWTViewSet, self).create(request, *args, **kwargs)
