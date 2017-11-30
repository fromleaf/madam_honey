#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView


class HoneyAppMainView(TemplateView):
    template_name = 'honey_app/main.html'

    def get_context_data(self, **kwargs):
        context = super(HoneyAppMainView, self).get_context_data(**kwargs)
        return context