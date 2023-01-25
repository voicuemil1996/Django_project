from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer

client = APIClient()

class TestProduct(TestCase):
    """ Test module for GET all products API """

    # def setUp(self):
    #     Product.objects.create(**product_test_dict)
    

    def test_create_product(self):
        """
        Test create a new object.
        """
        url = reverse('product_list')
        data = product_test_dict
        response = client.post(url, data, format='json')
        # error_message = "Something wnet worng./n" \
        #                 f"Response message:{response.}"
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_product(self):
        """
        Test delete an object.
        """
        url = reverse('product_detail', args=[test_product_title])
        response = client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_all_products(self):
    #     # get API response
    #     response = client.get(reverse('get_post_products'))
    #     # get data from db
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products, many=True)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    


test_product_title = "test_product_title"
product_test_dict = {
    "title": test_product_title,
    "price": 1.0,
    "description": "test_desc",
    "image": None,
    "category": "Pizza"
}

category_test_dict = {
    "title": "test_category_title",
    "description": "test_desc"
}

review_test_dict = {
    "rating": 1.0,
    "description": "test_desc",
    "product_title": "test_product_title"
}
