from django.shortcuts import render, HttpResponse
from . import models

recipes=[
  {
  'author': 'sandesh',
  'title': 'Chicken Masala',
  'directions': 'chicken masala',
  'date_posted': 'jan 23, 2024'
},
  {
  'author': 'sachin',
  'title': 'Paneer Masala',
  'directions': 'chicken masala',
  'date_posted': 'jan 03, 2024'
},
  {
  'author': 'sandesh',
  'title': 'Egg Masala',
  'directions': 'chicken masala',
  'date_posted': 'jan 13, 2024'
},
  {
  'author': 'sandesh',
  'title': 'Avalakki Sushila',
  'directions': 'chicken masala',
  'date_posted': 'jan 27, 2024'
}
]

def home(request):
  recipes = models.Recipe.objects.all()
  context={
    'recipes': recipes
  }
  return render(request, "recipes/home.html", context)


def about(request):
  return render(request, "recipes/about.html")


