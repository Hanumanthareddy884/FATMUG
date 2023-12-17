from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router =DefaultRouter()

router.register('vendors',views.VendorViewset,basename='vendor')
router.register('purchase_orders',views.PurchaseOrderViewset,basename='purchase_orders')

urlpatterns = [
    path('',include(router.urls)),
]
