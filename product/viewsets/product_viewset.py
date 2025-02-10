from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers import ProductSerializer


class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
