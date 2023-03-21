from django.db import models
from stock.models import StoreStock
from storerequest.models import StockRequest
from drug.models import Drug
# Create your models here.
class StockTransfer(models.Model):
    id= models.UUIDField(primary_key=True)
    from_stock_id= models.ForeignKey(StoreStock, on_delete=models.CASCADE)
    to_stock_id= models.ForeignKey(StoreStock, on_delete=models.CASCADE)
    request_id= models.ForeignKey(StockRequest, on_delete=models.CASCADE)
    transfer_status= models.BooleanField(default=True)
    transfer_desc= models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class TransferDrug(models.Model):
    id= models.UUIDField(primary_key=True)
    drug_id= models.ForeignKey(Drug, on_delete=models.CASCADE)
    transfer_id= models.ForeignKey(StockTransfer, on_delete=models.CASCADE)
    transfer_drug_quantity= models.IntegerField(min=1)
    transfer_drug_status= models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
