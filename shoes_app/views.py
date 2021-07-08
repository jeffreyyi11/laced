from django.shortcuts import render, HttpResponse
from user_app.models import User

# Create your views here.
def profile(request):
    context = {
        "user": User.objects.get(id = request.session["user_id"])
    }
    return render(request, "home.html", context)