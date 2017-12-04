#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from .serializers import UserSerializer, GroupSerializer


class UserViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_queryset(self):
        return super(UserViewSet, self).get_queryset()

    def create(self, request, *args, **kwargs):
        return super(UserViewSet, self).create(request, *args, **kwargs)


class GroupViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    required_scopes = ['groups']
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
