from django.contrib import admin
from .models import StockRequest, RequestDrug
# Register your models here.

admin.site.register(StockRequest)
admin.site.register(RequestDrug)