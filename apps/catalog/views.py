from django.shortcuts import render
from django.views import View

from rest_framework import generics


from . import models, serializers

# Create your views here.


class CategoriesAllView(View):
    def get(self, request):
        queryset = models.Category.objects.all()
        context = {
            'queryset': queryset
        }
        return render(request, 'catalog/index.html', context)


class ProductsListView(generics.ListAPIView):
    serializer_class = serializers.ProductListSerializer
    queryset = models.Product.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = serializers.ProductCreateSerializer

    # def perform_create(self, serializer):
    #     serializer.save()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductDetailSerializer
    queryset = models.Product.objects.all()
