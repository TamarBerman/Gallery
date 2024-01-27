from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("logoutPage/", views.logoutPage, name="logout"),
]
