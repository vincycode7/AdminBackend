from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
import random

from .models import Product, User
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
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
class UserAPIView(APIView):
    def get(self, request): #/api/products(get)
        users = User.objects.all()
        try:
            user = random.choice(users)
        except:
            return Response({"error" : "no user found"})
        return Response({"userId":user.id})

    def post(self, request): #/api/products(post)
        serializer = ProductSerializer(data=request.data)
        print("checking ",serializer)
        serializer.is_valid(raise_exception=True)
        print("checking ",serializer)
        serializer.save()
        print("checking ",serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk=None): # /api/products/<str:id>
        pass

    def delete(self, request, pk=None): # /api/products/<str:id>
        pass