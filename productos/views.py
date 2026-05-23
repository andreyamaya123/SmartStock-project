from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required

def lista_productos(request):
    productos = Producto.objects.all()

    return render(request, 'productos/lista.html', {
        'productos': productos
    })

@login_required
def agregar_producto(request):
    
    if request.method == 'POST':

        form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('lista_productos')
        
    else:
        form = ProductoForm()

    return render(request, 'productos/agregar.html', {
         'form' : form})

@login_required
def editar_producto(request, id):
    producto = Producto.objects.get(id=id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)

        if form.is_valid():
            form.save()
            return redirect('lista_productos')

    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productos/editar.html', {
        'form': form,
        'producto': producto
    })

@login_required
def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return redirect('lista_productos')

from django.shortcuts import render
from django.db.models import Sum, F
from .models import Producto


def dashboard(request):
    total_productos = Producto.objects.count()

    productos_agotados = Producto.objects.filter(stock=0).count()

    stock_bajo = Producto.objects.filter(stock__lt=5, stock__gt=0).count()

    valor_total = (
        Producto.objects.aggregate(
            total=Sum(F('precio') * F('stock'))
        )['total'] or 0
    )

    return render(request, 'productos/dashboard.html', {
        'total_productos': total_productos,
        'productos_agotados': productos_agotados,
        'stock_bajo': stock_bajo,
        'valor_total': valor_total,
    })

# Create your views here.
