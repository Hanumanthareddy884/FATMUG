from rest_framework import serializers
from .models import *


class VendorSeriliazer(serializers.ModelSerializer):
    class Meta:
        model =Vendor
        fields = '__all__'

class PurchaseOrderSeriliazer(serializers.ModelSerializer):
    class Meta:
        model =PurchaseOrder
        fields = '__all__'

class HistoricalPerformanceSeriliazer(serializers.ModelSerializer):
    class Meta:
        model =HistoricalPerformance
        fields = '__all__'