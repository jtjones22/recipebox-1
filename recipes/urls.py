from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index),
    path('authors/', views.author_detail),
    path('recipes/', views.recipe_detail)

    #path('admin/', admin.site.urls),
]