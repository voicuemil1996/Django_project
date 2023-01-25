Hello!
This project is about an online food store.

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