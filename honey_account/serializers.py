#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import JWToken


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        label='email', max_length=255,
        style={'input_type': 'email'},
    )
    password = serializers.CharField(
        style={'input_type': 'password'}, max_length=255,
        help_text='password'
    )

    class Meta:
        model = User
        fields = (
            'username', 'password', 'is_active', 'is_staff', 'date_joined'
        )
        write_only_fields = ('password',)


class CreateAccountSerializer(AccountSerializer):
    username = serializers.CharField(
        label='email', max_length=255,
        validators=[UniqueValidator(queryset=User.objects.all()), ],
        style={'input_type': 'email'},
    )

    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, max_length=255,
        help_text='for confirm password'
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'confirm_password',
        )

    def validate(self, data):
        # Check that the two password entries match
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise serializers.ValidationError(
                {"confirm_password": "confirm password doesn't match password."},
            )

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=self.validated_data["username"],
            password=self.validated_data["password"],
            email=self.validated_data["username"]
        )
        return user


class AccountWithJWTSerializer(AccountSerializer):
    token = serializers.CharField(read_only=True, source='get_jwt_token')

    class Meta:
        model = User

    def get_jwt_token(self):
        token = JWToken.objects.filter(
            user_id=self.id
        ).select_related('user_jwtoken')

        return token.last()


class CreateAccountWithJWTSerializer(AccountWithJWTSerializer):
    username = serializers.CharField(
        label='email', max_length=255,
        validators=[UniqueValidator(queryset=User.objects.all()), ],
        style={'input_type': 'email'},
    )

    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, max_length=255,
        help_text='for confirm password'
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'confirm_password',
            'token',
        )

    def create(self, validated_data):
        user = User.objects.create_user(
            username=self.validated_data["username"],
            password=self.validated_data["password"],
            email=self.validated_data["username"]
        )

        # create JWT
        JWToken.objects.create(user=user)

        return user
