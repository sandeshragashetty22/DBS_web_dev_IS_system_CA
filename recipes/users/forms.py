from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()
  mobile_number = forms.CharField(max_length=15, required=True)
  country = forms.CharField(max_length=50, required=True)
  age = forms.IntegerField(required=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2', 'mobile_number', 'country', 'age']

