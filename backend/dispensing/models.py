from django.db import models
from user.models import User
from store.models import Store
from stock.models import StoreStock
# Create your models here.


class Dispensing(models.Model):
    id= models.UUIDField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    total_price= models.FloatField(default=0.0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    


class SoldDrug(models.Model):
    id= models.UUIDField(primary_key=True)
    sold_quantity= models.IntegerField(min=1)
    sell_price= models.FloatField(default=0.0)
    dispensing_id= models.ForeignKey(Dispensing, on_delete=models.CASCADE)
    store_stock_id= models.ForeignKey(StoreStock, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    