#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.test.client import encode_multipart

from rest_framework import status

from honey_account.viewsets import UserViewSet

from .base import (
    add_middleware_to_request, add_middleware_to_response,
    BaseAccountAPITest
)


class AccountTest(BaseAccountAPITest):
    def test_create_account(self):
        """
        Create User Account (POST)
        :return:
        """

        data = {
            'username': "tester@test.com",
            'password': "123456",
        }
        content = encode_multipart('BoUnDaRyStRiNg', data)
        content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
        response = self.client.post(
            '/v1/accounts/users/', content, content_type=content_type
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(), self.base_account.TESTER_EMAIL)

    def test_get_user(self):
        request = self.factory.get('/accounts/v1/users/')
        request.user = AnonymousUser()

        # request is set tag by Sessions
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()

        # process test about request
        response = UserViewSet
        self.assertContains(response, "")
