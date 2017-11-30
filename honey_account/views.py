#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView

from rest_framework.generics import (
    CreateAPIView,
)

from honey_common.permissions import IsAuthenticatedOrCreate

from .forms import CreateAccountForm, LoginForm
from .serializers import UserSerializer


class SignUpAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrCreate, )


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CreateAccountForm
    success_url = '/thanks/'

    def form_valid(self, form):
        super(SignUpView, self).form_valid(form)

        # user = authenticate(
        #     self.request, username=self.object.username,
        #     password=self.object.password
        # )
        login(self.request, self.object)


        return redirect('/app/main/', user=self.object)

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        return context


class LogInView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = '/thanks/'

    def form_valid(self, form):
        return super(LogInView, self).form_valid(form)


class ThanksView(TemplateView):
    template_name = 'accounts/thanks.html'
