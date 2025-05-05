from django.db import models
import random
from users.models import Student

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
def generate_code():
    return ''.join(random.choice(CHARS) for _ in range(5))

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ShopHistory(models.Model):
    STATUTES = (
        ("Pending", "Pending"),
        ('Sold', 'Sold'),
        ('Returned', 'Returned'),
    )
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='shop_history')
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='shop_history')
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()
    code = models.CharField(max_length=50, default=generate_code())
    status = models.CharField(max_length=50, choices=STATUTES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.status}"


class BadgeCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Badge(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(BadgeCategory, on_delete=models.CASCADE, related_name='badges')
    icon = models.ImageField(upload_to='badges/')
    limit = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class MarsNews(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    banner = models.ImageField(upload_to='mars_news/')
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/')
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

