# from backendapp.apps.core.serializers import AttachmentSerializer, ReusableSerializer
from rest_framework import serializers
from .models import Inventory, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())

    class Meta:
        model = Inventory
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["supplier"] = SupplierSerializer(instance.supplier).data
        return response
