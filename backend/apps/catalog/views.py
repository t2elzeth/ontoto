import logging
import os

from django.shortcuts import render
from django.views import View
from django.conf import settings

from rest_framework import generics, permissions


from . import models, serializers


logging.basicConfig(
    filename=os.path.join(settings.BASE_DIR, 'app.log'),
    filemode='w',
    level=logging.INFO
)

# Create your views here.


class ProductsListView(generics.ListAPIView):
    serializer_class = serializers.ProductListSerializer
    queryset = models.Product.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = serializers.ProductCreateSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductDetailSerializer
    queryset = models.Product.objects.all()