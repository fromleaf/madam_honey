#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from oauth2_provider.views.mixins import OAuthLibMixin
from oauth2_provider.settings import oauth2_settings

from honey_common.viewsets import CreateViewSet, RDViewSet
from honey_common.permissions import IsAuthenticatedOrCreate
from .serializers import (
    AccountSerializer, SignUpSerializer
)


class AccountViewSet(RDViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all().order_by('id')
    serializer_class = AccountSerializer


class SignUpViewSet(CreateViewSet):
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = User.objects.all().order_by('id')
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        account_serializer = AccountSerializer(data=request.data)
        account_serializer.is_valid(raise_exception=True)
        account_serializer.save()

        return Response(account_serializer.data)


class SignUpWithOAuth2ViewSet(OAuthLibMixin, CreateViewSet):
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = User.objects.all().order_by('id')
    serializer_class = SignUpSerializer

    server_class = oauth2_settings.OAUTH2_SERVER_CLASS
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

    def create(self, request, *args, **kwargs):
        account_serializer = AccountSerializer(data=request.data)
        account_serializer.is_valid(raise_exception=True)
        account_serializer.save()

        url, headers, body, status = self.create_token_response(request)
        response = HttpResponse(content=body, status=status)

        for k, v in headers.items():
            response[k] = v

        return response
