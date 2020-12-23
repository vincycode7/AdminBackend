from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import random

from .models import Product, User
from .producer import publish
from .serializer import ProductSerializer, UserSerializer

# Create your views here. (APIView is used to concat different 
# functionalities into one class it helps reducing re-defining 
# the same set of code across models)
class ProductViewSet(viewsets.ViewSet):
    def list(self, request): #/api/products(get)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"products":serializer.data})

    def create(self, request): #/api/products(post)
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None): # /api/products/<str:id>
        product = get_object_or_404(Product,id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): # /api/products/<str:id>
        product = get_object_or_404(Product,id=pk)
        product.delete()
        publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
class UserAPIView(APIView):
    def get(self, request): #/api/products(get)
        users = User.objects.all()
        try:
            user = random.choice(users)
        except:
            return Response({"error" : "no user found"})
        return Response({"id":user.id})

    def post(self, request): #/api/products(post)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk=None): # /api/products/<str:id>
        pass

    def delete(self, request, pk=None): # /api/products/<str:id>
        pass