from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    document = models.FileField(upload_to="docs/")
    view_count = models.BigIntegerField()
    date_created = models.DateTimeField()
