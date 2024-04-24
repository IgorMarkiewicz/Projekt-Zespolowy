from django.http import HttpResponse
from django.shortcuts import render
from recipes.models import Allergen
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')

def allergen_list(request):
    allergens = Allergen.objects.all()
    return render(request, 'allergen_list.html', {'allergens': allergens})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def about(request):
    return render(request, 'about.html')
