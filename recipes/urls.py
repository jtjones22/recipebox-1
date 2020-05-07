from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index, name='Homepage'),
    path('author/<int:author_id>/', views.author_detail),
    path('recipe/<int:recipe_id>/', views.recipe_detail),
    path('addrecipe/', views.add_recipe),
    path('addauthor/', views.add_author),
    path('login/', views.login_view),
    path('logout/', views.logout_view)
]