from django.db.models import Count, Avg, Sum
from abc import ABC, abstractmethod

class BaseFilter(ABC):
    def __init__(self, product_obj, queryset) -> None:
        self.product_obj = product_obj
        self.queryset = queryset

    @abstractmethod
    def apply_filters(self):
        pass

    ############### Sorting methods ###############
    def apply_sorting(self):
        order_criteria = self.product_obj.request.query_params.get('order_by')
        if order_criteria is not None:
            self.treat_sorting_particular_cases(order_criteria)    
            self.sort_general_cases(order_criteria)

    def sort_general_cases(self, order_criteria):
        order_param = order_criteria
        order_sign = ''
        if ':' in order_criteria:
            order_way_options = ['ascending', 'asc', 'descending', 'desc']
            order_comps = order_criteria.split(':')
            order_param = order_comps[0]
            order_way = order_comps[1]
            if order_way not in order_way_options:
                raise ValueError(f"Order way parameter {order_way} is not valid./n"
                                    f"The accepted parameters are: {order_way_options}")
            if order_way in ['descending', 'desc']:
                order_sign = '-'

        self.queryset = self.queryset.order_by(f"{order_sign}{order_param}")

    @abstractmethod
    def treat_sorting_particular_cases(self, order_criteria):
        pass

    ############### Filter Methods ###############
    #todo: Implement filter with contains operator
    def apply_description_filter(self):
        description = self.product_obj.request.query_params.get('description')
        if description is not None:
            self.queryset = self.queryset.filter(description=description)

    def apply_count_filter(self):
        count = self.product_obj.request.query_params.get('count')
        if count is not None:
            self.queryset = self.queryset[:int(count)]


class ProductFilters(BaseFilter):
    
    def apply_filters(self):
        self.apply_sorting()
        self.apply_title_filter()
        self.apply_description_filter()
        self.apply_category_filter()
        self.apply_count_filter()
    
    ############### Sorting methods ###############
    def treat_sorting_particular_cases(self, order_criteria):
        if 'avg_rating' in order_criteria:
            self.queryset = self.queryset.annotate(avg_rating=Avg('review__rating'))
        if 'popularity' in order_criteria:
            self.queryset = self.queryset.annotate(popularity=Count('review'))
        if 'average_rating' in order_criteria:
            raise ValueError("Sorting by average rating cannot be done yet.")
    
    ############### Filter Methods ###############
    #todo: Implement two filters on the same time
    def apply_category_filter(self):
        category = self.product_obj.request.query_params.get('category')
        if category is not None:
            self.queryset = self.queryset.filter(category=category)

    #todo: Implement filter with contains operator
    def apply_title_filter(self):
        title = self.product_obj.request.query_params.get('title')
        if title is not None:
            self.queryset = self.queryset.filter(title=title)
    
    # todo: Implement price filter with comparison operators(eg. price>=10)
    def apply_price_filter(self):
        pass


class CategoryFilters(BaseFilter):

    def apply_filters(self):
        self.apply_sorting()
        self.apply_description_filter()
        self.apply_count_filter()
        
    
    ############### Sorting methods ###############
    def treat_sorting_particular_cases(self, order_criteria):
        if 'total_price' in order_criteria:
            self.queryset = self.queryset.annotate(total_price=Sum('product__price'))

    ############### Filter Methods ###############


class ReviewFilters(BaseFilter):

    def apply_filters(self):
        self.apply_sorting()
        self.apply_description_filter()
        self.apply_product_title_filter()
        self.apply_count_filter()
    
    ############### Sorting methods ###############
    def treat_sorting_particular_cases(self, order_criteria):
        pass

    ############### Filter Methods ###############
    # todo: Implement rating filter with comparison operators(eg. rating>=3)
    def apply_rating_filter(self):
        pass

    def apply_product_title_filter(self):
        product_title = self.product_obj.request.query_params.get('product_title')
        if product_title is not None:
            self.queryset = self.queryset.filter(product_title=product_title)
