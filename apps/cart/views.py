from django.shortcuts import render

from rest_framework import generics

from . import serializers

# Create your views here.


class CartProductCreateView(generics.CreateAPIView):
    serializer_class = serializers.CartProductCreateSerializer
