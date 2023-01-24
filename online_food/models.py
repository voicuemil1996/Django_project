from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    description = models.CharField(max_length=200, blank=True)


class Review(models.Model):  
    Stars = models.IntegerChoices('Stars', 'one_star two_stars three_stars four_stars five_stars')
    product_title = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Stars.choices)
    description = models.CharField(max_length=200, blank=True)
    

class Product(models.Model):    
    title = models.CharField(max_length=200, primary_key=True)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="images")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
