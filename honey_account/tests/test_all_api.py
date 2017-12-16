#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from django.contrib.auth.models import User, AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.test.client import encode_multipart

from rest_framework import status

from honey_account.viewsets import SignUpWithJWTViewSet

from .base import (
    add_middleware_to_request, BaseAccountAPITest
)


class AccountTest(BaseAccountAPITest):
    @unittest.skip("Not implemented")
    def test_create_account(self):
        """
        Create User Account (POST)
        :return:
        """
        data = {
            'username': "tester@test.com",
            'password': "123456",
            'confirm_password': "123456",
        }
        content = encode_multipart('BoUnDaRyStRiNg', data)
        content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
        view = SignUpWithJWTViewSet.as_view({'post': 'create'})

        # make request
        request = self.factory.post(
            '/v1/accounts/signup/', content, content_type=content_type
        )

        # request to view and get response
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(), self.base_account.TESTER_EMAIL)

    def test_create_account_with_jwt(self):
        """
        Create User Account with JWT (POST)
        :return:
        """
        data = {
            'username': "tester@test.com",
            'password': "123456",
            'confirm_password': "123456",
        }
        content = encode_multipart('BoUnDaRyStRiNg', data)
        content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
        view = SignUpWithJWTViewSet.as_view({'post': 'create'})

        # make request
        request = self.factory.post(
            '/v1/accounts/signup-jwt/', content, content_type=content_type
        )

        # request to view and get response
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(), self.base_account.TESTER_EMAIL)

    @unittest.skip("Not implemented")
    def test_get_user(self):
        request = self.factory.get('/accounts/v1/accounts/')
        request.user = AnonymousUser()

        # request is set tag by Sessions
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()

        # process test about request
