from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate

from recipes.models import Recipe, Author
from recipes.forms import AddRecipeForm, AddAuthorForm, LoginForm

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('Homepage'))
    form = LoginForm()
    return render(request, 'genericform.html')


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def author_detail(request, author_id):
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
    html = "genericform.html"

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
    html = 'genericform.html'

    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('Homepage'))

    form = AddAuthorForm()

    return render(request, html, {'form': form})
