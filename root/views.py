from django.shortcuts import render
from .models import Personnels, Food
# Create your views here.

def home(requests):
    personnels = Personnels.objects.filter(status = True)
    foods = Food.objects.filter(status = True)
    context = {
        'personnels' : personnels, 
        'foods' : foods,
    }
    return render(requests, 'root/index.html', context=context)