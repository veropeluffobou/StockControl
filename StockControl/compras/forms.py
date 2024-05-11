from django import forms
from .models import Producto, Proveedor

class ProductoForm(forms.ModelForm):
    # ModelChoiceField: representa un campo de opciones a partir de instancias de un Modelo predefinido.
    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all())

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual', 'proveedor']

class ProductoEditForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni']

class ProveedorEditForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido']