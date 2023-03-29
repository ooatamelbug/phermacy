from django.db import models
from uuid import uuid4
from user.models import User 

# Create your models here.

class Responsibilities(models.Model):
    resp_id=models.UUIDField(primary_key=True, default=uuid4)
    resp_name=models.CharField(max_length=15)
    resp_type=models.CharField(max_length=3)
    resp_action= models.CharField(max_length=3)
    resp_status= models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.resp_name
    


class UserResponsibilities(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid4)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    resp_id= models.ForeignKey(Responsibilities, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)

    def __str__(self):
        return self.user_id
