from django.db import models
from drug.models import Drug
from purchaseorder.models import PurchaseOrder

# Create your models here.
class PurchaseDrug(models.Model):
    purchase_drug_id=models.UUIDField(primary_key=True)
    order_quantity=models.IntegerField()
    invoice_quantity= models.IntegerField()
    drug_cost= models.FloatField()
    drug_id = models.ForeignKey(Drug, on_delete=models.CASCADE)
    order_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
