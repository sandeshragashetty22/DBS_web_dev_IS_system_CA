
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="recipe-register"),
    path('', views.profile, name="user-profile"),
]