#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from .base import BaseAccountTest


class AccountTest(BaseAccountTest):
    def test_create_account(self):
        user = self.create_user(email='random_user@random.com')
