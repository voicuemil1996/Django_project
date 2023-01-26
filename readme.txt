Hello!
This project is about an online restaurant.

Possible endpoints:
- categories/
- categories/{category_title}/
- products
- products/{product_title}
- reviews/
- reviews/{review_id}

Query parameters:
General Sorting: 
- order_by={sorting_field}:{asc/ascending/desc/descending}

General filters:
- count={given_number}
- description={description_field}

Product:
- Particular sorting: order_by=avg_rating; popularity(number of reviews)
- title={title_field}
- category={category-field}

Category:
- Particular sorting: order_by=total_price (sum of the product's prices under a certain category)

Review:
- product_title={product_title_field}

Examples:
/products/?category=Pizza&order_by=avg_rating:desc&count=2
/products/?category=Pizza&order_by=popularity:desc
/categories/?order_by=total_price:desc
/reviews/?product_title=pizza_margherita&order_by=rating

Pytest command eg.:
pytest .\online_food\tests.py
pytest .\online_food\tests.py::TestReview
pytest .\online_food\tests.py::TestReview::test_get_specific_review