from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [SearchFilter]
    search_fields = ['address']

    def get_queryset(self):
        queryset = Stock.objects.all()
        products = self.request.query_params.get('products')
        if products:
            queryset = queryset.filter(positions__product_id=products).distinct()
        return queryset
