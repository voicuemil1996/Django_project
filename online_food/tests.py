import pytest
from .test_utils import *


@pytest.mark.django_db
class TestCategory():

    def test_get_all_categories(self):
        
        category1 = Category()
        category1.create()
        category2 = Category(title="category_2")
        category2.create()

        category1.fetch_all()
        assert category1.response.status_code == 200
        assert len(category1.response.json()) == 2
        cleanup()

    def test_get_category(self):
        
        category1 = Category()
        category1.create()
        category1.fetch()

        assert category1.response.status_code == 200
        cleanup()

    def test_post_category(self):
        
        category1 = Category()
        category1.create()
        assert category1.response.status_code == 201
        cleanup()

    def test_put_category(self):
        
        category1 = Category()
        category1.create()

        category1.description = "updated description"
        category1.set_payload()
        category1.upgrade()
        assert category1.response.status_code == 200
        cleanup()

    def test_patch_category(self):
        
        category1 = Category()
        category1.create()

        category1.payload = {"description" : "updated description"}
        category1.update()
        assert category1.response.status_code == 200
        cleanup()

    def test_delete_category(self):
        
        category1 = Category()
        category1.create()

        category1.delete()
        assert category1.response.status_code == 204
        cleanup()


@pytest.mark.django_db
class TestProduct():

    def test_get_all_products(self):
        
        category1 = Product.pre_setup()
        product1 = Product(category1.title)
        product1.create()
        product2 = Product(category1.title, title="product2")
        product2.create()

        product1.fetch_all()
        assert product1.response.status_code == 200
        assert len(product1.response.json()) == 2
        cleanup()

    def test_get_product(self):
        
        category1 = Product.pre_setup()
        product1 = Product(category1.title)
        product1.create()

        product1.fetch()
        assert product1.response.status_code == 200
        cleanup()

    def test_post_product(self):
        
        category1 = Product.pre_setup()
        product1 = Product(category1.title)
        product1.create()
        assert product1.response.status_code == 201
        cleanup()

    def test_put_product(self):
        
        category1 = Product.pre_setup()
        product1 = Product(category1.title)
        product1.create()

        product1.description = "updated description"
        product1.set_payload()
        product1.upgrade()
        assert product1.response.status_code == 200
        cleanup()

    def test_patch_product(self):
        
        category1 = Product.pre_setup()
        product1 = Product(category1.title)
        product1.create()

        product1.payload = {"description" : "updated description"}
        product1.update()
        assert product1.response.status_code == 200
        cleanup()

    def test_delete_product(self):
        
        category1 = Product.pre_setup()
        product1 = Product(category1.title)
        product1.create()

        product1.delete()
        assert product1.response.status_code == 204
        cleanup()


@pytest.mark.django_db
class TestReview():

    def test_get_all_reviews(self):
        
        product1 = Review.pre_setup()
        review1 = Review(product1.title)
        review1.create()
        review2 = Review(product1.title)
        review2.create()

        review1.fetch_all()
        assert review1.response.status_code == 200
        assert len(review1.response.json()) == 2
        cleanup()


    def test_get_review(self):
        
        product1 = Review.pre_setup()
        review1 = Review(product1.title)
        review1.create()

        review1.fetch()
        assert review1.response.status_code == 200
        cleanup()

    def test_post_review(self):
        
        product1 = Review.pre_setup()
        review1 = Review(product1.title)
        review1.create()
        assert review1.response.status_code == 201
        cleanup()

    def test_put_review(self):
        
        product1 = Review.pre_setup()
        review1 = Review(product1.title)
        review1.create()

        review1.description = "updated description"
        review1.set_payload()
        review1.upgrade()
        assert review1.response.status_code == 200
        cleanup()

    def test_patch_review(self):
        
        product1 = Review.pre_setup()
        review1 = Review(product1.title)
        review1.create()

        review1.payload = {"description" : "updated description"}
        review1.update()
        assert review1.response.status_code == 200
        cleanup()

    def test_delete_review(self):
        
        product1 = Review.pre_setup()
        review1 = Review(product1.title)
        review1.create()

        review1.delete()
        assert review1.response.status_code == 204
        cleanup()
