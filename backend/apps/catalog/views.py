import datetime

from rest_framework import generics, permissions

from . import models, serializers


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
    serializer_class = serializers.ProductRetrieveUpdateDestroySerializer
    queryset = models.Product.objects.all()

    def perform_update(self, serializer):
        instance = self.get_object()

        if not instance.price == self.validated_data.get('price'):
            self.validated_data['old_price'] = instance.price

        self.validated_data['changes_number'] += 1
        self.validated_data['date_last_changed'] = datetime.date.today()

        serializer.save()
