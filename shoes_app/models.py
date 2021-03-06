from django.db import models
from user_app.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class ProfileManager(models.Manager):
    def profile_validator(self, profile_data):
        errors = {}
        if len(profile_data["location"]) <= 0:
            errors["location"] = "Please enter location"
        return errors

class Profile(models.Model):
    location = models.CharField(max_length = 20)
    rating = models.IntegerField(default = 0)
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ProfileManager()
    # shoes = list of shoes

class ShoeManager(models.Manager):
    def shoe_validator(self, shoe_data):
        errors = {}
        if len(shoe_data["brand"]) <= 0:
            errors["brand"] = "Please enter shoe brand"
        if len(shoe_data["style"]) <= 0:
            errors["style"] = "Please enter shoe style"
        if len(shoe_data["color"]) <= 0:
            errors["color"] = "Please enter shoe color"
        if shoe_data['size'] < 0:
            errors['size'] = "Please enter a shoe size"
        if shoe_data['rating'] < 1:
            errors['rating'] = "Please rate your shoe condition"
        return errors

class Shoes(models.Model):
    brand = models.CharField(max_length = 20)
    style = models.CharField(max_length = 50)
    color = models.CharField(max_length = 50)
    size = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    profile = models.ForeignKey(Profile, related_name = "shoes", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShoeManager()