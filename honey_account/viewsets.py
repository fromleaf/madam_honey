#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from honey_common.viewsets import CUViewSet, RDViewSet
from .serializers import (
    AccountSerializer, CreateAccountSerializer
)


class AccountViewSet(RDViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all().order_by('id')
    serializer_class = AccountSerializer


class CreateAccountViewSet(CUViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all().order_by('id')
    serializer_class = CreateAccountSerializer

    def create(self, request, *args, **kwargs):
        return super(CreateAccountViewSet, self).create(request, *args, **kwargs)
