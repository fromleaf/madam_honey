#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from channels.routing import route

from .consumers import ws_connect, ws_receive, ws_disconnect

channel_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_receive),
    route("websocket.disconnect", ws_disconnect),
]
