#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import User


class CreateAccountForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    username = forms.CharField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username', )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CreateAccountForm, self).save(commit=False)
        if commit:
            user = User.objects.create_user(
                username=self.cleaned_data["username"],
                password=self.cleaned_data["password1"]
            )
        return user


class AccountInfoChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    username = forms.CharField(label='Email', widget=forms.EmailInput)
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'password', 'is_active', 'is_staff')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.ModelForm):
    """
    A form for logging users.
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    username = forms.CharField(label='Email', widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ('username', 'password')
