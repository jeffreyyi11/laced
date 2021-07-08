from django.urls import path
from . import views
from shoes_app import templates

urlpatterns = [
    path("", views.login),
    path("registration", views.register),
    path("signup", views.signup),
]