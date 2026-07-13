from django.contrib import admin
from .models import Personnels, Category, Skills, Food, Features
# Register your models here.

admin.site.register(Personnels)
admin.site.register(Category)
admin.site.register(Skills)
admin.site.register(Food)
admin.site.register(Features)