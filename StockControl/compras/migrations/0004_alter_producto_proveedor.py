# Generated by Django 5.0.3 on 2024-03-29 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_alter_producto_stock_actual_alter_proveedor_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='compras.proveedor'),
        ),
    ]
