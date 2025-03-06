# Generated by Django 5.1 on 2025-03-06 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('note', models.TextField(blank=True, null=True)),
                ('stock', models.IntegerField(default=0)),
                ('availability', models.BooleanField(default=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to='inventory.supplier')),
            ],
        ),
    ]
