#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vikander.settings")
channel_layer = channels.asgi.get_channel_layer()
