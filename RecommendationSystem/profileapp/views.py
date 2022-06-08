from threading import _profile_hook
from django.shortcuts import render
from .models import Profile
# Create your views here.

def profile_view(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    #print(help(profile))
    return render(request, 'profileapp/profile.html', {'profile':profile})

def edit_profile(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        gender = request.POST["gender"]
        age = request.POST["age"]
        if "image" in request.FILES:
            profile.profile_picture = request.FILES["image"]
        
        profile.first_name = first_name
        profile.last_name = last_name
        profile.gender = gender
        profile.age = int(age)
        profile.save()
        return render(request, 'profileapp/profile.html', {'profile':profile})
    else:
        return render(request, 'profileapp/edit_profile.html', {'profile':profile})