from rest_framework import serializers
from .models import *


class VendorSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class PurchaseOrderSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class AcknowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['acknowledgment_date']


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg',
                  'average_response_time', 'fulfillment_rate']