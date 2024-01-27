from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.conf import settings


def register(request):
    if request.method == "POST": 
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/gallery")
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form":form})



def logoutPage(request):
    logout(request)
    return redirect('/login')


