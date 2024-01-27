from django.urls import path
from . import views


urlpatterns = [
    path('chat/<str:recipient_username>/', views.chat_view, name='chat'),
    path('user_detail/<str:username>/', views.user_detail, name='user_detail'),
    
]