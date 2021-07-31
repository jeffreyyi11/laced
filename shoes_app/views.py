from django.shortcuts import render, redirect
from user_app.models import User
from user_app.urls import *
from shoes_app.models import Shoes
from django.contrib import messages

# Create your views here.
def profile(request):
    user = User.objects.get(id = request.session["user_id"]),
    context = {
        "user": user
    }
    return render(request, "home.html", context)

def logout(request):
    request.session.flush()
    return redirect("/")

def shoeform(request):
    if "user_id" not in request.session:
        return redirect("/")
    return render(request, "shoeform.html")

def addshoe(request):
    errors = Shoes.objects.shoe_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return render(request, "shoeform.html")
    else: 
        user = User.objects.get(id=request.session['user_id'])
        user_profile = user.profile
        shoe = Shoes.objects.create(
            brand = request.POST['brand'],
            style = request.POST['style'],
            color = request.POST['color'],
            size = request.POST['size'],
            rating = request.POST['rating'],
            profile = user_profile
        )
        return redirect("/addshoe")