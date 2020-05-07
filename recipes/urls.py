from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index, name='Homepage'),
    path('author/<int:author_id>/', views.author),
    path('recipe/<int:recipe_id>/', views.recipe_detail),
    path('addrecipe/', views.add_recipe),
    path('addauthor/', views.add_author)
    #path('admin/', admin.site.urls),
]