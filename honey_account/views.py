#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView

from rest_framework.generics import (
    CreateAPIView,
)

from honey_common.permissions import IsAuthenticatedOrCreate

from .models import HoneyUser
from .forms import ContactForm, LoginForm
from .serializers import SignUpSerializer


class SignUpAPIView(CreateAPIView):
    queryset = HoneyUser.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate, )


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        return super(SignUpView, self).form_valid(form)

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
