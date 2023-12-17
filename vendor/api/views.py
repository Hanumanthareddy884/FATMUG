from django.shortcuts import render
from .seriliazers import *
from .models import *
from rest_framework import viewsets


# Create your views here.
class VendorViewset(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSeriliazer

class PurchaseOrderViewset(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSeriliazer

    def get_queryset(self,*args):
        return PurchaseOrder.objects.filter(vendor_id=1)
