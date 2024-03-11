from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from . import forms

def register(request):
  if request.method == "POST":
    form = forms.UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f"{username}, you're account is created, please login.")
      return redirect('user-login')
  else:
    form = forms.UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    user = request.user
    form = forms.UserRegisterForm(instance=user)

    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('user-profile')

    context = {'form': form}
    return render(request, 'users/profile.html', context)
