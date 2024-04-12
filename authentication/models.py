from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", default="main.jpg")
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    liked_blogs = models.ManyToManyField(to="base.Blog")
    USERNAME_FIELD = "username"
