from django.urls import path
from . import views

from chat_app.views import chat_view


urlpatterns = [
    path('', views.home, name='Home'),
    path('home', views.home, name='Home'),
    path('gallery', views.gallery, name='Gallery'),
    path('gallery/<int:image_id>', views.image, name='Image'),
    path('gallery/addreview/<int:image_id>/', views.addreview, name='addreview'),
    path('chat/<str:recipient_username>/', chat_view, name='chat_view'),


]
