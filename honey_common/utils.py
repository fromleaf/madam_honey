#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone


def get_local_today():
    now = timezone.localtime(timezone.now())
    return now
