from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import models


class RecipeListView(ListView):
  model = models.Recipe
  template_name = 'recipes/home.html'
  context_object_name = 'recipes'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['categories'] = models.Recipe.CATEGORY_CHOICES
    return context


def home(request):
  category = models.Recipe.objects.values_list('category', flat=True).distinct()
  recipes = models.Recipe.objects.all()
  context = {
    'category': category,
    'recipes': recipes
  }
  return render(request, 'recipes/home.html', context)

def category_recipes(request, category):
  recipes = models.Recipe.objects.filter(category=category)
  context = {
    'category': category,
    'recipes': recipes
  }
  return render(request, 'recipes/category_recipes.html', context)

def about(request):
  return render(request, 'recipes/about.html', {'title': 'about page'})

class RecipeDetailView(DetailView):
  model = models.Recipe
  template_name = 'recipes/recipe_detail.html'
  context_object_name = 'recipes'

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = models.Recipe
  success_url = reverse_lazy('recipes-home')
  template_name = 'recipes/recipe_confirm_delete.html'
  context_object_name = 'recipes'

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

class RecipeCreateView(LoginRequiredMixin, CreateView):
  model = models.Recipe
  fields = ['title', 'description',  'category']
  template_name = 'recipes/recipe_form.html'
  context_object_name = 'recipes'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = models.Recipe
  fields = ['title', 'description',  'category']
  template_name = 'recipes/recipe_form.html'
  context_object_name = 'recipes'

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)