from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="shoes"),
    path("signout", views.logout, name="sign_out"),
    path("shoeform", views.shoeform, name="shoe_form"),
    path("addshoe", views.addshoe, name="add_shoe")
]