from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "registration.html")

def signup(request):
    if request.POST["access"] == "register":
        errors = User.objects.registration_validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/registration")
        else:
            hashed_pw = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
            registered = User.objects.create(email = request.POST["email"], password = hashed_pw)
            request.session["user_id"] = registered.id
            return redirect("/shoes")
    if request.POST["access"] == "login":
        errors = User.objects.login_validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            user = User.objects.get(email = request.POST["email"])
            request.session["user_id"] = user.id
            return redirect("/shoes")
