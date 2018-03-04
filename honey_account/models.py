#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

from rest_framework_jwt.settings import api_settings


class TokenModel(models.Model):
    """
    Default Token Model.
    """
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class JWToken(TokenModel):
    user = models.ForeignKey(
        User, related_name='user_jwtoken', on_delete=models.CASCADE
    )
    payload = models.CharField(max_length=100, null=False)
    token = models.CharField(max_length=300, null=False)
    expires = models.IntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        self.payload = jwt_payload_handler(self.user)
        self.token = jwt_encode_handler(self.payload)
        self.expired_time = self.payload.get('exp', None)

        super(JWToken, self).save()


class RefreshJWToken(TokenModel):
    user = models.ForeignKey(
        User, related_name='user_jwtoken', on_delete=models.CASCADE
    )
    access_token_id = models.BigIntegerField(null=False)
    token = models.CharField(max_length=300, null=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(RefreshJWToken, self).save()
