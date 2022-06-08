import email
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# Create your views here.
from profileapp.models import Profile
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'username':username, 'password':password, 'error': True})
    else:
        return render(request, 'accounts/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']      
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.filter(username=username).first()
            if user is not None:
                return render(request, 'accounts/signup.html', {'username':username, 'password':password1, 'error1': 'Username already exists'})
            else:
                user = User.objects.create_user(username, '', password1)
                try:
                    profile = Profile()
                    profile.user = user
                    profile.save()
                except Exception as e:
                    user.delete()
                    print(e)
                    return redirect('home')
                login(request, user)
                return redirect('home')
        
        else:
            return render(request, 'accounts/signup.html', {'username':username, 'error2': "Passwords didn't matched"})
    else:
        return render(request, 'accounts/signup.html')

def logout_view(request):
    logout(request)
    return redirect('home')