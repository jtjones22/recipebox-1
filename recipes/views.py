from django.shortcuts import render, reverse, HttpResponseRedirect

from recipes.models import Recipe
from recipes.models import Author
from recipes.forms import AddRecipeForm, AddAuthorForm

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def author(request, author_id):
    author = Author.objects.get(id=author_id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'author_detail.html', {
        'author': author,
        'recipes': recipes
    })




def recipe_detail(request, recipe_id):
    recipes = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipes': recipes})


def add_recipe(request):
    html = 'addrecipeform.html'

    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title = data['title'],
                author = data['author'],
                description = data['description'],
                time_required = data['time_required'],
                instructions = data['instructions']
            )
            return HttpResponseRedirect(reverse('Homepage'))


    form = AddRecipeForm()

    return render(request, html, {"form": form})

def add_author(request):
    html = 'addauthorform.html'

    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('Homepage'))

    form = AddAuthorForm()

    return render(request, html, {'form': form})
