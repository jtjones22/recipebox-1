from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index, name='Homepage'),
    path('authors/<int:author_id>/', views.author_detail),
    path('recipes/<int:recipe_id>/', views.recipe_detail),
    path('recipeadd/', views.recipeadd),
    #path('admin/', admin.site.urls),
]