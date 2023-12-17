from django.shortcuts import render
from rest_framework.response import Response
from .seriliazers import *
from .models import *
from rest_framework import viewsets, permissions
from rest_framework.generics import UpdateAPIView,RetrieveAPIView
from django.utils import timezone

# Create your views here.
class VendorViewset(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSeriliazer
    permission_classes = [permissions.IsAuthenticated]

class PurchaseOrderViewset(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSeriliazer
    permission_classes =[permissions.IsAuthenticated]


class AcknowledgeUpdate(UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = AcknowledgeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.validated_data['acknowledgment_date'] = timezone.now()
        super().perform_update(serializer)
        return Response(serializer.data)

# Retrieve performance details of a specific vendor


class VendorPerformance(RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [permissions.IsAuthenticated]
