from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length=120)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)
    
class Personnels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='root', default='image.jpg')
    content = models.TextField(default='he is really good at making coffee')
    skills = models.ManyToManyField(Skills)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ('created_at',)
    

class Features(models.Model):
    name = models.CharField(max_length=120)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)
        
class Category(models.Model):
    name = models.CharField(max_length=120)
    features = models.ManyToManyField(Features)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)
        
class Food(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField(default='tastes so delicious')
    category = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    old_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    recommend = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)
    