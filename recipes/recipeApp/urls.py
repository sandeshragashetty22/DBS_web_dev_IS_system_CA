
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('about/', views.about, name="recipe-about"),
]