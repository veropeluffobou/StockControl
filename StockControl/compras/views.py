from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm, ProductoEditForm, ProveedorEditForm


def home(request):
    return render(request, 'index.html')

# -------------------------------------------------------- #
#                        PRODUCTOS                         #
# -------------------------------------------------------- #

# READ
def listarProductos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

# CREATE
def crearProducto(request):
    proveedores = Proveedor.objects.all() # pasar el contexto de la DB de proveedores al formulario
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos_listado')
        else:
            mensaje = "Por favor, complete todos los campos del formulario."
            return render(request, 'crear_producto.html', {'form': form, 'mensaje': mensaje, 'proveedores': proveedores})
    else:
        form = ProductoForm()

    return render(request, 'crear_producto.html', {'form': form, 'proveedores': proveedores})

# UPDATE
def editarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoEditForm(request.POST, instance=producto)   
        if form.is_valid():
                form.save()
                return redirect('productos_listado')
        else:
            mensaje = "Por favor, complete todos los campos del formulario."
            return render(request, 'crear_producto.html', {'form': form, 'producto': producto, 'mensaje': mensaje})  
    else:
        form = ProductoEditForm()

    return render(request, 'crear_producto.html', {'form': form, 'producto': producto})


# DELETE
def borrarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos_listado')
    return render(request, 'borrar_producto.html', {'producto': producto})


# -------------------------------------------------------- #
#                       PROVEEDORES                        #
# -------------------------------------------------------- #

# READ
def listarProveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

# CREATE
def crearProveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores_listado')
        else:
            mensaje = "Por favor, complete todos los campos del formulario."
            return render(request, 'crear_proveedor.html', {'form': form, 'mensaje': mensaje})

    else:
            form = ProveedorForm()

    return render(request, 'crear_proveedor.html')

# UPDATE
def editarProveedor(request, dni):
    
    proveedor = get_object_or_404(Proveedor, dni=dni)
    if request.method == 'POST':
        form = ProveedorEditForm(request.POST, instance=proveedor)   
        if form.is_valid():
                form.save()
                return redirect('proveedores_listado')
        else:
            mensaje = "Por favor, complete todos los campos del formulario."
            return render(request, 'crear_proveedor.html', {'form': form, 'proveedor': proveedor, 'mensaje': mensaje})  
    else:
        form = ProveedorEditForm()

    return render(request, 'crear_proveedor.html', {'form': form, 'proveedor': proveedor})


# DELETE
def borrarProveedor(request, dni):
    proveedor = get_object_or_404(Proveedor, dni=dni)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedores_listado')
    return render(request, 'borrar_proveedor.html', {'proveedor': proveedor})