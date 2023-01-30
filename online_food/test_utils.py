from django.urls import reverse
from rest_framework.test import APIClient
from abc import abstractmethod


#TODO: Implement cleanup as pytest fixture
client = APIClient()

category_list = 'category_list'
review_list = 'review_list'
product_list = 'product_list'
category_detail = 'category_detail'
review_detail = 'review_detail'
product_detail = 'product_detail'

def cleanup():
    for api_object in BaseApi.junk:
        api_object.delete()
        print(f"Object of type {type(api_object)} deleted")


class BaseApi():
    junk = []

    def __init__(self):
        self.payload = ""
        self.response = {}
        self.url_detail = ""
        self.set_payload()

    # GET
    def fetch(self):
        """
        Do a get request using current object URL
        :return: request's response
        """

        response = client.get(self.url_detail)
        print('GET', response.json(), response.status_code, sep='\n')
        self.response = response
        return response
    
    def fetch_all(self):
        """
        Do a get request using current object URL
        :return: request's response
        """

        response = client.get(self.URL_LIST)
        print('GET', response.json(), response.status_code, sep='\n')
        self.response = response
        return response

    # POST
    def create(self):
        print(self.payload)
        response = client.post(self.URL_LIST, self.payload)
        print('POST', response.json(), response.status_code, sep='\n')
        self.response = response
        BaseApi.junk.append(self)

    # PATCH
    def update(self):
        response = client.patch(self.url_detail, self.payload)
        print('PATCH', response.json(), response.status_code, sep='\n')
        self.response = response
        # if response.status_code == 422:
        #     print(self.payload)
        #     raise HTTPError(url=self.API_URL, code=response.status_code, msg=response.json(), hdrs=self.api_key, fp='')

    # PUT
    def upgrade(self):
        response = client.put(self.url_detail, self.payload)
        print('PUT', response.json(), response.status_code, sep='\n')
        self.response = response
        # if response.status_code == 422:
        #     print(self.payload)
        #     raise HTTPError(url=self.API_URL, code=response.status_code, msg=response.json(), hdrs=self.api_key, fp='')

    # DELETE
    def delete(self):
        response = client.delete(self.url_detail)
        print('DELETE', response.status_code, sep='\n')
        self.response = response
        # if response.status_code == 404:
        #     print(self.payload)
        #     raise HTTPError(url=self.API_URL, code=response.status_code, msg=response.json(), hdrs=self.api_key, fp='')
 
    # PAYLOAD
    @abstractmethod
    def set_payload(self):
        pass

class Product(BaseApi):
    URL_LIST = reverse(product_list)

    def __init__(self, category, title="test_product", description="test", price=1.0, image=""):
        self.title = title
        self.description = description
        self.price = price
        self.image = image
        self.category = category
        self.url_detail = reverse(product_detail, args=[title])
        super().__init__()

    def set_payload(self):
        self.payload = {
            "title": self.title,
            "description" : self.description,
            "price": self.price,
            "image": self.image,
            "category": self.category
        }
    
    def create(self):
        super().create()
        self.url_detail = reverse(product_detail, args=[self.title])

    @staticmethod
    def pre_setup():
        category_obj = Category()
        category_obj.create()

        return category_obj
    

class Category(BaseApi):
    URL_LIST = reverse(category_list)

    def __init__(self, title="test_category", description="test"):
        self.title = title
        self.description = description
        super().__init__()

    def set_payload(self):
        self.payload = {
            "title": self.title,
            "description" : self.description,
        }
    
    def create(self):
        super().create()
        self.url_detail = reverse(category_detail, args=[self.title])


class Review(BaseApi):
    URL_LIST = reverse(review_list)

    def __init__(self, product_title, rating=1, description="test"):
        self.id = ""
        self.product_title = product_title
        self.description = description
        self.rating = rating 
        super().__init__()

    def set_payload(self):
        self.payload = {
            "rating": self.rating,
            "description" : self.description,
            "product_title": self.product_title
        }

    def create(self):
        super().create()
        self.id = self.response.json()['id']
        self.url_detail = reverse(review_detail, args=[self.id])

    @staticmethod
    def pre_setup():
        category_obj = Category()
        category_obj.create()

        product_obj = Product(category=category_obj.title)
        product_obj.create()

        return product_obj
