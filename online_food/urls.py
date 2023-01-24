from .views import *
from django.urls import path
from .enpoints import *

urlpatterns = [
    
    path('', index, name="index"),
    path(categories, CategoryList.as_view(), name="category_list"),
    path(categories_details, CategoryDetail.as_view(), name="category_detail"),
    path(products, ProductList.as_view(), name="product_list"),
    path(product_details, ProductDetail.as_view(), name="product_detail"),
    # todo: Make the reviews url to be nested to products 
    path(reviews, ReviewList.as_view(), name="review_list"),
    path(reviews_details, ReviewDetail.as_view(), name="review_detail"),
]
