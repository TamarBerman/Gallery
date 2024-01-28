from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# UserCreationForm is a built-in Django form for user registration with a username and password.
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    anonymous = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        
        model = User # indicates that the form is associated with the User model, which is part of Django's built-in authentication system
        fields = ["username", "email", "password1", "password2", "anonymous"]
