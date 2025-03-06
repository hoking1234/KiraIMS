from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api import InventoryViewSet, SupplierViewSet
from .views import inventory_detail, inventory_list, supplier_list

app_name = "inventory"

router = DefaultRouter()
router.register(r"api/inventory", InventoryViewSet, basename="inventory_api")
router.register(r"api/supplier", SupplierViewSet, basename="supplier_api")

urlpatterns = [
    path("", include(router.urls)),
    path("inventory/", inventory_list, name="inventory_list"),
    path("inventory/<int:id>/", inventory_detail, name="inventory_detail"),
    path("supplier/", supplier_list, name="inventory_list"),
]
