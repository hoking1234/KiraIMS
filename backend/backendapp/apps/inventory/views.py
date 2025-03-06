from django.shortcuts import render, get_object_or_404
from .models import Inventory
from .api import InventoryViewSet
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


def inventory_list(request):
    return render(request, "inventory/list.html", {})


def inventory_detail(request, id):
    inventory = get_object_or_404(Inventory, id=id)
    return render(request, "inventory/detail.html", {"inventory": inventory})


def supplier_list(request):
    return render(request, "supplier/list.html", {})
