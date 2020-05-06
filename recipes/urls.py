from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index, name='Homepage'),
    path('author/<int:author_id>/', views.author_detail),
    path('recipe/<int:recipe_id>/', views.recipe_detail),
    path('recipeadd/', views.recipeadd),
    path('authoradd/', views.authoradd)
    #path('admin/', admin.site.urls),
]