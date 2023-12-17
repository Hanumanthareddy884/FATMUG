from django.contrib import admin
from .models import Vendor,PurchaseOrder,HistoricalPerformance
# Register your models here.
admin.site.register([Vendor,PurchaseOrder,HistoricalPerformance])