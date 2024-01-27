from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User

# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('chat', recipient_username=user.username)
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})



# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('chat', recipient_username=user.username)
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})



@login_required(login_url='/login')
def chat_view(request, recipient_username):    
    if not request.user.username == recipient_username:
        # Redirect to the chat URL with the username of the currently logged-in user
        return redirect('chat_view', recipient_username=request.user.username)
 
    context={'recipient_username': recipient_username}
    return render(request, 'chat.html',context)



# def logout_view(request):
#     logout(request)
#     return redirect('/login')



# # returns users details

def user_detail(request, username):
    try:
        user = User.objects.get(username=username)
        user_details = {
            'username': user.username,
            'email': user.email,
        }
        return JsonResponse(user_details)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

