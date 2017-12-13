#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView

from .forms import CreateAccountForm, LoginForm


class SignupView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CreateAccountForm
    success_url = '/app/main/'

    def form_valid(self, form):
        super(SignupView, self).form_valid(form)
        # This user has to login after created user.
        login(self.request, self.object)
        return redirect('/app/main/', user=self.object)

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        return context


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect('/app/main/', user=user)
        else:
            return redirect('/account/signup/')


class LogoutView(TemplateView):
    template_name = 'accounts/login.html'

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('/main/')


class ThanksView(TemplateView):
    template_name = 'accounts/thanks.html'
