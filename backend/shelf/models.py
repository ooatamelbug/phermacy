from django.db import models
from store.models import Store
from stock.models import StoreStock
# Create your models here.

class Shelf(models.Model):
    id= models.IntegerField(primary_key=True)
    shelf_name= models.CharField(max_length=25)
    shelf_location= models.CharField(max_length=25)
    store_id= models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.shelf_name
    

class ShelfDrug(models.Model):
    id= models.IntegerField(primary_key=True)
    shelf_id = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    store_stock_id = models.ForeignKey(StoreStock, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    