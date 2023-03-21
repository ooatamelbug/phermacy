from django.db import models
from drug.models import Drug
from store.models import Store

# Create your models here.
class Stock(models.Model):
    id= models.UUIDField(primary_key=True)
    en_name= models.CharField(max_length=25)
    ar_name= models.CharField(max_length=25)
    stock_quantity= models.IntegerField()
    const_price= models.FloatField()
    selling_price=models.FloatField()
    durg_id= models.ForeignKey(Drug,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.en_name
    


class StoreStock(models.Model):
    id= models.UUIDField(primary_key=True)
    store_quantity= models.IntegerField()
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.store_quantity

    