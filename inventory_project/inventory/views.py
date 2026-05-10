from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product, Order
from .forms import OrderForm
from django.db import models
from django.db.models import Sum

def product_list(request):
    products= Product.objects.all()
    return render(request, 'inventory/product_list.html',{'products':products})

from django.shortcuts import render, redirect
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'inventory/add_product.html', {'form': form})

from django.shortcuts import get_object_or_404

def update_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'inventory/update_product.html', {'form': form})

def delete_product(request,id):
    product=get_object_or_404(Product, id=id)

    if request.method=='POST':
        product.delete()
        return redirect('product_list')
    return render(request,'inventory/delete_product.html',{'product':product})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            product = order.product

            if order.quantity > product.quantity:
                return render(request, 'inventory/create_order.html', {
                    'form': form,
                    'error': 'Not enough stock!'
                })

            product.quantity -= order.quantity
            product.save()

            order.save()
            return redirect('product_list')
    else:
        form = OrderForm()

    return render(request, 'inventory/create_order.html', {'form': form})

def order_list(request):
    orders=Order.objects.all().order_by('-created_at')
    return render(request,'inventory/order_list.html',{'orders':orders})

def update_order(request,id):
    order=Order.objects.get(id=id)
    if request.method=='POST':
        order.status=request.POST.get('status')
        order.save()
        return redirect('order_list')
    
    return render(request,'inventory/update_order.html',{'order':order})

def dashboard(request):
    total_products=Product.objects.count()
    total_orders=Order.objects.count()
    low_stock=Product.objects.filter(quantity__lte=models.F('reorder_level')).count()

    context = {
        'total_products': total_products,
        'total_orders': total_orders,
        'low_stock': low_stock
    }

    return render(request, 'inventory/dashboard.html', context)

def product_list(request):
    query=request.GET.get('q')

    if query:
        products=Product.objects.filter(name__icontains=query)
    else:
        products=Product.objects.all()

    return render(request, 'inventory/product_list.html',{
        'products':products
    })

