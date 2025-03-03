from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import UserProfile
# Create your views here.

def login(request):
    
    user = None
    if "user" in request.session: 
        user = User.objects.get(username=request.session["user"])
    
    if request.method == "GET":
        config = {
            "user": user,
            "userprofile": UserProfile.objects.get(user=user) if user else None
        }
        return render(request, "login.html", config)
    else:
        username = request.POST["username"]
        password = request.POST["Password"]
        
        
        if authenticate(username=username, password=password):
            
            request.session["user"] = username
            return redirect(profile)
        else:
            return redirect(signup)


def signup(request):
    
    if request.method == "GET":
        user = None
        if "user" in request.session: user = User.objects.get(username=request.session["user"])
        
        config = {
            "user": user,
            "userprofile": UserProfile.objects.get(user=user) if user else None
        }
        return render(request, "signup.html", config)
    else:
        username = request.POST["username"]
        password = request.POST["Password"]
        
        # =================================================================================== #
        try :
            user = User.objects.create_user(username=username, password=password)
            UserProfile.objects.create(user=user, profile_picture=request.FILES['profile_picture'])
        except :
            return redirect(signup)
        # =================================================================================== #
        
        return redirect(login)


def profile(request):
    
    user = None
    if "user" in request.session: 
        user = User.objects.get(username=request.session["user"])
        
        config = {
            "user": user,
            "userprofile": UserProfile.objects.get(user=user) if user else None
        }
        return render(request, "profile.html", config)
    else:
        return redirect(login) 


def logout(request):

    if "user" in request.session: 
        request.session.pop("user")
    
    return redirect(login)