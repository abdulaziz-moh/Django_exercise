from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 150)
    password = models.CharField(max_length = 128) # stores the password hash
    email = models.EmailField()
    phone = models.CharField(max_length = 12)
    registration_datetime = models.DateTimeField( auto_now=True, auto_now_add=True) # not sure still
    user_type = models.CharField(max_length = 50)



# # inside the forms.py
# from django import forms

# class UserForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)