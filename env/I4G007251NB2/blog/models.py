from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    Title=models.CharField(max_length=200)
    Text=models.TextField()
    Author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    Created_date=models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    Published_date=models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    