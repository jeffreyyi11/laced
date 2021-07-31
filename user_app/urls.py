from django.urls import path
from . import views
from shoes_app import templates

urlpatterns = [
    path("", views.login, name="user_login"),
    path("registration", views.register, name="user_signup"),
    path("signup", views.signup),
]