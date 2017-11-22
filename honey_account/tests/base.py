#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from django.contrib.auth.models import User
from django.test.client import RequestFactory

from oauth2_provider.models import get_application_model

from rest_framework.test import APITestCase


pytest_mark = pytest.mark.django_db
Application = get_application_model()


class BaseAccountTest(APITestCase):
    def setUp(self):
        """
        This function will execute before test case starts
        :return: nothing
        """
        # To get all sql queries sent by Django from py shell
        self.TEST_USER = "test_user"
        self.ADMIN_USER = "admin_user"
        self.PASSWORD = "123456"
        self.EMAIL = "fromleaf@gmail.com"
        self.NORMAL_USER_NAME = "gildong"
        self.NORMAL_PASSWORD = "test"
        self.KOREAN_NAME = "홍길동"
        self.PHONE = "01099991111"

        self.admin_token = ""
        self.test_token = ""
        self.factory = RequestFactory()

        test_user = User(username=self.TEST_USER, email=self.EMAIL)
        test_user.set_password(self.PASSWORD)
        test_user.save()

    def tearDown(self):
        """
        This function will execute after test case finished or got exception
        :return: nothing
        """
        pass

    def get_token(self, username, password, application, client):
        pass

    def create_randomic_users(self, user_count):
        user_arr = []
        for person in range(user_count):
            user_arr.append(
                User(
                    username='{0}{1}'.format('Anonymous', person),
                    email='{0}{1}@{2}.com'.format('Anonymous', person, person),
                    password='{0}'.format('MyPassW@')
                )
            )
        User.objects.bulk_create(user_arr)
        self.assertEqual(User.objects.count(), user_count)
