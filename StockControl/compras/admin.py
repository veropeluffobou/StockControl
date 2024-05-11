from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Producto, Proveedor


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'dni']
    search_fields = ['nombre', 'apellido', 'dni']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'precio', 'stock_actual', 'proveedor']
    list_filter = ('proveedor__nombre', 'proveedor__apellido')    
    search_fields = ['nombre', 'precio', 'proveedor__nombre', 'proveedor__apellido']


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)