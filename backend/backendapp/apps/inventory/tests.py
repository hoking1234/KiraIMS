from django.test import TestCase, Client
from django.urls import reverse
from .models import Inventory, Supplier


class InventoryTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.supplier = Supplier.objects.create(name="Test Supplier")
        self.inventory_obj = Inventory.objects.create(
            name="Test Item",
            description="A sample inventory item.",
            note="Test note.",
            stock=10,
            availability=True,
            supplier=self.supplier,
        )

    def test_inventory_page(self):
        response = self.client.get("/inventory/")
        self.assertEqual(response.status_code, 200)

    def test_inventory_api(self):
        response = self.client.get("/api/inventory/")
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_page(self):
        response = self.client.get(f"/inventory/{self.inventory_obj.id}/")
        self.assertEqual(response.status_code, 200)
