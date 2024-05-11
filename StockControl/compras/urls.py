from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('compras', views.home, name="home"),

    path('compras/productos', views.listarProductos, name="productos_listado"),
    path('compras/productos/listado', views.listarProductos, name="productos_listado"),
    path('compras/productos/crear', views.crearProducto, name="productos_crear"),
    path('compras/productos/editar/<int:id>', views.editarProducto, name='editar_producto'), 
    path('compras/productos/borrar/<int:id>', views.borrarProducto, name='borrar_producto'),

    path('compras/proveedores', views.listarProveedores, name="proveedores_listado"),
    path('compras/proveedores/listado', views.listarProveedores, name="proveedores_listado"),
    path('compras/proveedores/crear', views.crearProveedor, name="proveedores_crear"),
    path('compras/proveedores/editar/<int:dni>', views.editarProveedor, name='editar_proveedor'), 
    path('compras/proveedores/borrar/<int:dni>', views.borrarProveedor, name='borrar_proveedor'),

]