#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from honey_common import utils


class CommonModel(models.Model):
    """
    Default Model.
    All models aren't removed on database, but they look like to be removed.
    """
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted = utils.get_local_today()
        self.save()
