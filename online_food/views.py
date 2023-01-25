from rest_framework import generics
from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from django.http import HttpResponse
from .enpoints import *
from .filters import ProductFilters, CategoryFilters, ReviewFilters


def index(request):
    #todo:beautify the below on html page
    return HttpResponse("Read the readme.txt")
                        # ("URLs:/n")
                        # f"{categories}/n"
                        # f"{categories_details}/n"
                        # f"{products}/n"
                        # f"{product_details}/n"
                        # f"{reviews}/n"
                        # f"{reviews_details}/n")


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        queryset = Category.objects.all()
        category_filter = CategoryFilters(self, queryset)
        category_filter.apply_filters()
        return category_filter.queryset


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        product_filter = ProductFilters(self, queryset)
        product_filter.apply_filters()
        return product_filter.queryset


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        queryset = Review.objects.all()
        review_filter = ReviewFilters(self, queryset)
        review_filter.apply_filters()
        return review_filter.queryset


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
