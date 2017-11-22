from django.shortcuts import render

from rest_framework.generics import (
    CreateAPIView,
)
from django.contrib.auth.models import User

from honey_common.permissions import IsAuthenticatedOrCreate
from .serializers import SignUpSerializer


class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate, )
