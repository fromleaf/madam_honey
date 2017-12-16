#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from django.contrib.auth.models import User
from django.test.testcases import TestCase
from django.test.client import RequestFactory

from rest_framework.test import APITestCase, APIClient


pytest_mark = pytest.mark.django_db


def add_middleware_to_request(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request


def add_middleware_to_response(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request


class BaseAccountTest(TestCase):
    def setUp(self):
        """
        This function will execute before test case starts
        :return: nothing
        """
        # To get all sql queries sent by Django from py shell
        # Common Info
        self.PASSWORD = "123456"
        self.PHONE = "01099991111"

        # Admin Info
        self.ADMIN = "admin"
        self.ADMIN_EMAIL = "admin@test.com"

        # Tester Info
        self.TESTER = "tester"
        self.TESTER_EMAIL = "tester@test.com"

        # USER Info
        self.USER = "gildong"
        self.USER_EMAIL = "gildong@gildong.com"

        self.admin_token = ""
        self.test_token = ""

        # create admin, tester and user
        self.admin = User.objects.create_superuser(
            username=self.ADMIN_EMAIL, email=self.ADMIN_EMAIL,
            password=self.PASSWORD,
        )
        self.tester = User.objects.create_user(
            username=self.TESTER_EMAIL, email=self.TESTER_EMAIL,
            password=self.PASSWORD,
        )
        self.user = User.objects.create_user(
            username=self.USER_EMAIL, email=self.USER_EMAIL,
            password=self.PASSWORD,
        )

    def tearDown(self):
        """
        This function will execute after test case finished or got exception
        :return: nothing
        """
        pass

    def get_token(self, password, application, client):
        pass

    @staticmethod
    def create_user(email=None):
        created_user = User.objects.create_user(
            username=email, password='{0}'.format('MyPassW@'), email=email
        )
        return created_user

    @staticmethod
    def create_random_users(user_count):
        user_arr = []
        for person in range(user_count):
            user_arr.append(
                User(
                    username='{0}_{1}@anonymous.com'.format('anonymous', person),
                    password='{0}'.format('MyPassW@'),
                    email='{0}_{1}@anonymous.com'.format('anonymous', person),
                )
            )
        created_users = User.objects.bulk_create(user_arr)
        return created_users


class BaseAccountAPITest(APITestCase):
    def setUp(self):
        self.base_account = BaseAccountTest()
        self.factory = RequestFactory()
        self.client = APIClient()

    def tearDown(self):
        """
        This function will execute after test case finished or got exception
        :return: nothing
        """
        pass
