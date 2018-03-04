# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import mixins, viewsets


class CRUDViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """
    A viewset that provides
    'create', 'update', 'list', 'retrieve', and 'delete' actions.
    """
    pass


class RDViewSet(mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    """
    A viewset that provides 'list', 'retrieve', and 'delete' actions.
    """
    pass


class CreateViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    """
    A viewset that provides only 'create' actions.
    """
    pass

