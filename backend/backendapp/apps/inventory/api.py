from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Inventory, Supplier
from .serializers import InventorySerializer, SupplierSerializer
from .utils import query_inspect


class ReusableViewSet(viewsets.ModelViewSet):
    @query_inspect  # Decorator to inspect the number of queries and time taken by the function
    def list(self, request, *args, **kwargs):
        try:
            query_params = request.query_params
            self.queryset = self.queryset.filter(**query_params.dict())
            response = super().list(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response(e, status=status.HTTP_200_OK)


class InventoryViewSet(ReusableViewSet):
    queryset = Inventory.objects.select_related("supplier").all()
    serializer_class = InventorySerializer


class SupplierViewSet(ReusableViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
