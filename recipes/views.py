from django.shortcuts import render, reverse, HttpResponseRedirect

from recipes.models import Recipe
from recipes.models import Author
from recipes.forms import RecipeAddForm, AuthorAddForm

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def author(request, author_id):
    author = Author.objects.get(id=author_id)
    recipes = Recipe.objects.filter(author==author)
    return render(request, 'author_detail.html', {
        'author': author,
        'recipes': recipes
    })


def author_detail(request):
    authors = Author.objects.all()
    return render(request, 'author_detail.html', {'authors': authors})


def recipe_detail(request, recipe_id):
    recipes = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipes': recipes})


def recipeadd(request):
    html = 'recipeaddform.html'

    if request.method == "POST":
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title = data['title'],
                author = data['author'],
                description = data['description'],
                time_required = data['time_required'],
                instructions = data['instructions']
            )
            return HttpResponseRedirect(reverse('homepage'))


    form = RecipeAddForm()

    return render(request, html, {"form": form})

def authoradd(request):
    html = 'authoraddform.html'

    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AuthorAddForm()

    return render(request, html, {'form': form})
