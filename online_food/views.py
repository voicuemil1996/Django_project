from rest_framework import generics
from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from django.http import HttpResponse
from django.core.serializers import serialize
from .enpoints import *


def index(request):
    #todo:beautify the below on html page
    return HttpResponse("URLs:/n")
                        # f"{categories}/n"
                        # f"{categories_details}/n"
                        # f"{products}/n"
                        # f"{product_details}/n"
                        # f"{reviews}/n"
                        # f"{reviews_details}/n")


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        queryset = Review.objects.all()
        product_title = self.request.query_params.get('product_title')

        queryset = Review.objects.all()
        if product_title is not None:
            queryset = queryset.filter(product_title=product_title)
        return queryset


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
