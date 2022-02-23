from rest_framework import viewsets
from core.api import serializers


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = serializers.ProductTypeSerializer.Meta.model.objects.all()
    serializer_class = serializers.ProductTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = serializers.ProductSerializer.Meta.model.objects.all()
    serializer_class = serializers.ProductSerializer