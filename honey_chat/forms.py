#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import ChatRoom


class CreateChatRoomForm(forms.ModelForm):

    class Meta:
        model = ChatRoom
        fields = ('name', )
