from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index, name='Homepage'),
    path('author/<int:author_id>/', views.author_detail),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('addrecipe/', views.add_recipe),
    path('addauthor/', views.add_author),
    path('recipe/edit/<int:recipe_id>/', views.edit_recipe_view, name='edit_recipe'),
    path('recipe/favorite/<int:recipe_id>', views.favorite, name='favorite'),
    path('recipe/unfavorite/<int:recipe_id>', views.unfavorite, name='unfavorite'),
    path('recipes/favorited/<int:user_id>', views.favorites, name='favorites'),


    #path('admin/', admin.site.urls),
]