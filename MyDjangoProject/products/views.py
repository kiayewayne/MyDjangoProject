from django.shortcuts import render, redirect
from .models import Product, Category
from django import forms

# Simple Django form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'description', 'image']

# Add product view
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

# Display all products
def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list_products.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})
