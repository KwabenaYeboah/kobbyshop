from django.shortcuts import render, get_object_or_404
from cart.forms import AddProductToCartForm

from .models import Category, Product

def product_list_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(availability=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    return render(request, 'products/product_list.html',
                  {'category':category, 'categories':categories, 'products':products})

def product_detail_view(request, slug, pk):
    product = get_object_or_404(Product, slug=slug, pk=pk, availability=True)
    form = AddProductToCartForm()
    return render(request, 'products/product_detail.html', 
                  {'product':product, 'form':form})
    
    