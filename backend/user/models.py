from django.db import models
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class User(BaseUserManager):
    data= models.BooleanField(default=False) 