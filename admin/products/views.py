from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializer

# Create your views here.
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
    
    def update(self, request, pk=None): # /api/products/<str:id>
        pass

    def retrieve(self, request, pk=None): # /api/products/<str:id>
        pass

    def detroy(self, request, pk=None): # /api/products/<str:id>
        pass

# Create your views here.
class ProductViewSet2(APIView):
    def list(self, request): #/api/products(get)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"products":serializer.data})

    def create(self, request): #/api/products(post)
        serializer = ProductSerializer(data=request.data)
        print("checking ",serializer)
        serializer.is_valid(raise_exception=True)
        print("checking ",serializer)
        serializer.save()
        print("checking ",serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None): # /api/products/<str:id>
        pass

    def retrieve(self, request, pk=None): # /api/products/<str:id>
        pass

    def detroy(self, request, pk=None): # /api/products/<str:id>
        pass