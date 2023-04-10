from django.db import models
from store.models import Store
from drug.models import Drug
# Create your models here.

class StockRequest(models.Model):
    id= models.IntegerField(primary_key=True)
    request_desc= models.TextField()
    request_status= models.BooleanField(default=True)
    store_id= models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class RequestDrug(models.Model):
    id= models.IntegerField(primary_key=True)
    drug_id= models.ForeignKey(Drug, on_delete=models.CASCADE)
    request_drug_quantity= models.IntegerField()
    request_status= models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
