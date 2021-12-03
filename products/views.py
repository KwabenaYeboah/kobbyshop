from django.shortcuts import render, get_object_or_404
from cart.forms import AddProductToCartForm

from .recommendations import Recommend
from .models import Category, Product

def product_list_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(availability=True)
    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category, translations__language_code=language, 
                                     translations__slug=category_slug)
        products = products.filter(category=category)
    
    return render(request, 'products/product_list.html',
                  {'category':category, 'categories':categories, 'products':products})

def product_detail_view(request, slug, pk):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product, pk=pk, translations__slug=slug, 
                                translations__language_code=language, availability=True)
    form = AddProductToCartForm()
    
    # Recommend other products to users
    conn = Recommend()
    recommended_products = conn.suggest_products_for([product], max_results=4)
    return render(request, 'products/product_detail.html', 
                  {'product':product, 'form':form, 
                   'recommended_products':recommended_products})
    
    