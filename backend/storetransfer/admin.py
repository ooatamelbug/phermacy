from django.contrib import admin
from .models import StockTransfer, TransferDrug

# Register your models here.
admin.site.register(StockTransfer)
admin.site.register(TransferDrug)