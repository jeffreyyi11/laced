from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Model):
    def registration_validator(self, postData):
        errors = {}
        if len(postData["username"]) < 5:
            errors["username"] = "Username must be at least 5 character"
        users = User.objects.filter(username = postData["username"])
        if len(users) > 0:
            errors["username"] = "Username is already registered"
        Email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not Email_regex.match(postData['email']):
            errors['email'] = "Incorrect email!"
        user = User.objects.filter(email = postData['email'])
        if len(user) > 0:
            errors['unique_email'] = "Email already registered"
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be at least 8 character"
        if postData["password"] != postData["confirm"]:
            errors["password"] = "Passwords don't match"

    def login_validator(self, postData):
        errors = {}
        users = User.objects.filter(email = postData["email"])
        if len(users) == 0:
            errors['no_email'] = "Email not found"
        else:
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()) != True:
                errors['login_password'] = "Incorrect password!"
        return errors

class User(models.model):
    username = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Profile(models.model):
    first_name = models.CharField(blank = True)
    last_name = models.CharField(blank = True)
    state = models.CharField(max_length = 2)
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
