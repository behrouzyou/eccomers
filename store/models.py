from django.db import models
from django.db.models import Avg ,Count
from django.urls import reverse

from accounts.models import Account
from category.models import Category


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500,blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='photos/products')
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug,self.slug])



    def __str__(self):
        return self.product_name
    
    def avarageReview(self):
        reviews = ReviewRaiting.objects.filter(product=self,status=True).aggregate(average=Avg('rating'))

        return float(reviews['average'] or 0)
    
    def countReview(self):
        reviews = ReviewRaiting.objects.filter(product=self,status=True).aggregate(count=Count('id'))
        
        return int(reviews['count'] or 0)





    
class VariationManager(models.Manager):
    def colors(self):
        return super().filter(variation_category='color', is_active=True)
    def sizes(self):
        return super().filter(variation_category='size', is_active=True)


    

variation_category_choice = (
    ('color', 'Color'),
    ('size', 'Size'),

)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    objects = VariationManager()

    def __str__(self):
        return self.product.product_name + ' - ' + self.variation_category
    
    
class ReviewRaiting(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=200, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject 


    
