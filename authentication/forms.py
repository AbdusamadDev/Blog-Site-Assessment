from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ["username", "email"]

    # def clean_password_confirm(self):
    #     password = self.cleaned_data.get("password1")
    #     password_confirm = self.cleaned_data.get("password_confirm")

    #     if password and password_confirm and password != password_confirm:
    #         raise forms.ValidationError("Passwords do not match")
    #     return password_confirm
