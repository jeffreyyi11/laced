from django.urls import path
from . import views

urlpatterns = [
    path("", views.login),
    path("registration", views.register),
    path("signup", views.signup),
]