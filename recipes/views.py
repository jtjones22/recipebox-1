from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required


from recipes.models import Recipe
from recipes.models import Author
from recipes.forms import AddRecipeForm, AddAuthorForm

# Create your views here.
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
    html = "addrecipeform.html"

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

@login_required
def edit_recipe_view(request, recipe_id):
    html = 'edit_recipe.html'
    recipe = Recipe.objects.get(id=recipe_id)
    if request.user.id == recipe.author.id or request.user.is_staff:
        if request.method == 'POST':
            form = AddRecipeForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                recipe.title = data['title']
                recipe.description = data['description']
                recipe.time_required = data['time_required']
                recipe.instructions = data['instructions']
                recipe.save()
                return HttpResponseRedirect(reverse('recipe_detail', args=(recipe_id,)))
        form = AddRecipeForm(initial={
            'title': recipe.title,
            'author': recipe.author,
            'description': recipe.description,
            'time_required': recipe.time_required,
            'instructions': recipe.instructions
        })
        context = {'form': form}
        return render(request, html, context)
    else:
        return HttpResponseRedirect(reverse('recipe_detail', args=(recipe_id,)))


@login_required
def favorite(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    user = request.user.id
    recipe.favorited_by.add(user)
    recipe.save()
    return HttpResponseRedirect(reverse('recipe_detail', args=(recipe_id,)))


@login_required
def unfavorite(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    user = request.user.id
    recipe.favorited_by.remove(user)
    recipe.save()
    return HttpResponseRedirect(reverse('recipe_detail', args=(recipe_id,)))


def favorites(request, user_id):
    html = 'favorites.html'
    recipes = Recipe.objects.filter(favorited_by=user_id)
    context = {'recipes': recipes}
    return render(request, html, context)