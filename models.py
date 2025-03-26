from django.db import models
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Restorantlar(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news/images')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Mahsulotlar(models.Model):
    mahsulot_name = models.CharField(max_length=255)
    mahsulot_image = models.ImageField(upload_to='news/images')
    mahsulot_body = models.TextField(max_length=255, null=True ,blank=True)
    mahsulot_narx = models.DecimalField(max_digits=10, decimal_places=3)
    restorant_id = models.ForeignKey(Restorantlar, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.mahsulot_name

class User(models.Model):
    user_name = models.CharField(max_length=255)  
    user_phone_number = models.CharField(max_length=15) 
    user_address_title = models.CharField(max_length=255)  
    user_home_address = models.CharField(max_length=255)  
    user_address_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
