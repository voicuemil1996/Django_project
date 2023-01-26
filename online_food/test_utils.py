from django.urls import reverse
from rest_framework.test import APIClient
from time import sleep

#TODO: make the testing framework to be more oop oriented
client = APIClient()

category_list = 'category_list'
review_list = 'review_list'
product_list = 'product_list'
category_detail = 'category_detail'
review_detail = 'review_detail'
product_detail = 'product_detail'


category_title = "test_category_title"
category_test_dict = {
    "title": category_title,
    "description": "test_desc"
}

product_title = "test_product_title"
product_test_dict = {
    "title": product_title,
    "price": 1.0,
    "description": "test_desc",
    "image": "",
    "category": category_title
}

review_test_dict = {
    "rating": 1,
    "description": "test_desc",
    "product_title": product_title
}

class TestProductUtils():
    products_created = []

    @staticmethod
    def clean_up():
        for title in TestProductUtils.products_created:
            url = reverse(product_detail, args=[title])
            client.delete(url)

    @staticmethod
    def set_up_product():
        url = reverse(category_list)
        response = client.post(url, category_test_dict)
        print(f"Setup product: {response.data}")
    
    @staticmethod
    def create_products():
        TestProductUtils.set_up_product()
        for i in range(0,2):
            product_test_dict["title"] = product_test_dict["title"] + str(i)
            url = reverse(product_list)
            response = client.post(url, product_test_dict)
            TestProductUtils.products_created.append(response.data['title'])

    @staticmethod
    def get_product_title():
        """Populate the database with Product entities
        and return first entry's title
        """
        TestProductUtils.create_products()
        url = reverse(product_list)
        return client.get(url).data[0]['title']
    

class TestCategoryUtils():
    
    categories_created = []

    @staticmethod
    def clean_up():
        for title in TestCategoryUtils.categories_created:
            url = reverse(category_detail, args=[title])
            client.delete(url)

    @staticmethod
    def create_categories():
        for i in range(0,3):
            category_test_dict["title"] = category_test_dict["title"] + str(i)
            url = reverse(category_list)
            response = client.post(url, category_test_dict)
            print(response.data)
            TestCategoryUtils.categories_created.append(response.data['title'])

    @staticmethod
    def get_category_title():
        """Populate the database with Category entities
        and return first entry's title
        """
        TestCategoryUtils.create_categories()
        url = reverse(category_list)
        return client.get(url).data[0]['title']
    
class TestReviewUtils():
    
    reviews_created = []

    @staticmethod
    def clean_up():
        for id in TestReviewUtils.reviews_created:
            url = reverse(review_detail, args=[id])
            client.delete(url)

    @staticmethod
    def set_up_review():
        TestProductUtils.set_up_product()
        url = reverse(product_list)
        response = client.post(url, product_test_dict)
        print(response.data)
    
    @staticmethod
    def create_reviews():
        TestReviewUtils.set_up_review()
        for i in range(0,2):
            url = reverse(review_list)
            response = client.post(url, review_test_dict)
            print(response.data)
            TestReviewUtils.reviews_created.append(response.data['id'])

    @staticmethod
    def get_review_id():
        """Populate the database with Review entities
        and return first entry's id
        """
        TestReviewUtils.create_reviews()
        url = reverse(review_list)
        return client.get(url).data[0]['id']
