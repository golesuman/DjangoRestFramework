from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer


# Create your views here.
@api_view()
def product_list(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view()
def get_product(request, id):
    product = Product.objects.get(pk= id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)