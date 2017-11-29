#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.test import APITestCase


class BaseTest(APITestCase):
    def setUp(self):
        """
        This function will execute before test case starts
        :return: nothing
        """
        pass

    def tearDown(self):
        """
        This function will execute after test case finished or got exception
        :return: nothing
        """
        pass

    def get_token(self, password, application, client):
        pass

    def create_user(self, user_count):
        pass
