import pytest
from .test_utils import *
from .test_utils import TestCategoryUtils as tcu
from .test_utils import TestProductUtils as tpu
from .test_utils import TestReviewUtils as tru


@pytest.mark.django_db
class TestReview():

    def test_get_all_review(self):
        tru.create_reviews()
        url = reverse(review_list)
        response = client.get(url)
        assert response.status_code == 200
        tru.clean_up()

    def test_get_specific_review(self):
        title = tru.get_review_id()
        url = reverse(review_detail, args=[title])
        response = client.get(url)
        assert response.status_code == 200
        tru.clean_up()

    def test_create_new_review(self):
        tru.set_up_review()
        url = reverse(review_list)
        response = client.post(url, review_test_dict)
        assert response.status_code == 201
        tru.clean_up()

    def test_update_review(self):
        title = tru.get_review_id()
        review_test_dict['description'] = 'Updated description'
        url = reverse(review_detail, args=[title])
        response = client.put(url, review_test_dict)
        print(response.data)
        assert response.status_code == 200
        tru.clean_up()
        
    def test_patch_update_review(self):
        title = tru.get_review_id()
        url = reverse(review_detail, args=[title])
        response = client.patch(url, {'description':'patch_updated'})
        assert response.status_code == 200
        tru.clean_up()

    def test_delete_review(self):
        title = tru.get_review_id()
        url = reverse(review_detail, args=[title])
        response = client.delete(url)
        assert response.status_code == 204
        tru.clean_up()

@pytest.mark.django_db
class TestProduct():

    def test_get_all_products(self):
        tpu.create_products()
        url = reverse(product_list)
        response = client.get(url)
        assert response.status_code == 200
        tpu.clean_up()

    def test_get_specific_product(self):
        title = tpu.get_product_title()
        url = reverse(product_detail, args=[title])
        response = client.get(url)
        assert response.status_code == 200
        tpu.clean_up()

    def test_create_new_product(self):
        tpu.set_up_product()
        url = reverse(product_list)
        response = client.post(url, product_test_dict)
        assert response.status_code == 201
        tpu.clean_up()

    def test_update_product(self):
        title = tpu.get_product_title()
        product_test_dict['description'] = 'Updated description'
        url = reverse(product_detail, args=[title])
        response = client.put(url, product_test_dict)
        print(response.data)
        assert response.status_code == 200
        tpu.clean_up()
        
    def test_patch_update_product(self):
        title = tpu.get_product_title()
        url = reverse(product_detail, args=[title])
        response = client.patch(url, {'description':'patch_updated'})
        assert response.status_code == 200
        tpu.clean_up()

    def test_delete_product(self):
        title = tpu.get_product_title()
        url = reverse(product_detail, args=[title])
        response = client.delete(url)
        assert response.status_code == 204
        tpu.clean_up()


@pytest.mark.django_db
class TestCategory():    

    def test_get_all_categories(self):
        tcu.create_categories()
        url = reverse(category_list)
        response = client.get(url)
        assert response.status_code == 200
        tcu.clean_up()

    def test_get_specific_category(self):
        title = tcu.get_category_title()
        url = reverse(category_detail, args=[title])
        response = client.get(url)
        assert response.status_code == 200
        tcu.clean_up()

    def test_create_new_category(self):
        url = reverse(category_list)
        response = client.post(url, category_test_dict)
        assert response.status_code == 201
        tcu.clean_up()

    def test_update_category(self):
        title = tcu.get_category_title()
        category_test_dict['description'] = 'Updated description'
        url = reverse(category_detail, args=[title])
        response = client.put(url, category_test_dict)
        print(response.data)
        assert response.status_code == 200
        tcu.clean_up()

    def test_patch_update_category(self):
        title = tcu.get_category_title()
        url = reverse(category_detail, args=[title])
        response = client.patch(url, {'description':'patch_updated'})
        assert response.status_code == 200
        tcu.clean_up()

    def test_delete_product(self):
        title = tcu.get_category_title()
        url = reverse(category_detail, args=[title])
        response = client.delete(url)
        assert response.status_code == 204
        tcu.clean_up()
   