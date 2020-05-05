from django.shortcuts import render

from recipes.models import Recipe
from recipes.models import Author

# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})

def author_detail(request):
    authors = Author.objects.all()
    return render(request, 'author_detail.html', {'authors': authors})

def recipe_detail(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_detail.html', {'recipes': recipes})