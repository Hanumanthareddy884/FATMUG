from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router =DefaultRouter()

router.register('api/vendors',views.VendorViewset,basename='vendor')
router.register('api/purchase-orders',views.PurchaseOrderViewset,basename='purchase_orders')

urlpatterns = [
    path('',include(router.urls)),
    path('api/purchase-orders/<int:pk>/acknowledge/',
         views.AcknowledgeUpdate.as_view()),
    path('api/vendors/<int:pk>/performance/',
         views.VendorPerformance.as_view()),
]
