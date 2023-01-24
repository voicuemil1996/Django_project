from rest_framework import serializers
from rest_framework.fields import Field, empty
from .models import Product, Category, Review

        
class ProductSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField('get_average_rating_value')
    reviews_count = serializers.SerializerMethodField('get_reviews_count')

    def get_average_rating_value(self, obj):
        ratings_tuples = Review.objects.all().filter(product_title=obj.title).values_list('rating')
        if not len(ratings_tuples):
            return '-'
        ratings_values = [rating_tuple[0] for rating_tuple in ratings_tuples]
        return sum(ratings_values)/len(ratings_values)
        
    def get_reviews_count(self, obj):
        reviews_count = Review.objects.all().filter(product_title=obj.title)
        return len(reviews_count)
    
    class Meta:
        model = Product
        fields = ('title', 'price', 'description', 'image', 'category', 'avg_rating', 'reviews_count')


class CategorySerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField('get_total_price_value')

    def get_total_price_value(self, obj):
        prices_tuples = Product.objects.all().filter(category=obj.title).values_list('price')
        prices_values = [price_tuple[0] for price_tuple in prices_tuples]
        return sum(prices_values)
    
    class Meta:
        model = Category
        fields = ('title', 'description', 'total_price')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('__all__')
