from django.urls import path
from . import views


urlpatterns = [
    path('chat/<str:recipient_username>/', views.chat_view, name='chat'),    
]