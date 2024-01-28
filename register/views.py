from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.conf import settings


def register(request):
    # form is being submitted.
    if request.method == "POST": 
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            #  logs in the user
            login(request, user)
            return redirect("/home")
    else:
        # display form
        form = RegisterForm()
    return render(request, "register/register.html", {"form":form})



def logoutPage(request):
    #  provided by Django to log out the currently authenticated user.
    logout(request)
    return redirect('/login')


