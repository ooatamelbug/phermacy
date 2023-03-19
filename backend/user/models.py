from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
# Create your models here.

class User(AbstractUser):
    username = None
    first_name= models.CharField(max_length=15)
    last_name= models.CharField(max_length=15)
    middle_name= models.CharField(max_length=15)
    login_email = models.EmailField(unique=True, null=True)
    login_type= models.CharField(max_length=15) 
    user_status= models.BooleanField(default=True)
    login_id=models.CharField(max_length=15,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD= 'login_email'
    REQUIRED_FIELDS= []
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name