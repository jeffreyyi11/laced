from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def registration_validator(self, register_data):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(register_data["email"]):
            errors["email"] = "Invalid Email Address"
        if len(register_data["password"]) < 8:
            errors["password"] = "Password must be at least 8 characters"
        if register_data["password"] != register_data["confirm_password"]:
            errors["match"] = "Passwords need to match"
        return errors
    
    def login_validator(self, login_data):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(login_data["email"]):
            errors["email"] = "Invalid Login"
        users = User.objects.filter(email = login_data["email"])
        if len(users) == 0:
            errors["not_found"] = "Invalid Login"
        else:
            if users[0].email != login_data["email"]:
                errors["email_match"] = "Invalid Login"
            if not bcrypt.checkpw(login_data["password"].encode(), users[0].password.encode()):
                errors["pw_match"] = "Invalid Login"
        return errors

class User(models.Model):
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()