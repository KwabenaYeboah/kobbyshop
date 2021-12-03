from django.shortcuts import render, redirect ,get_object_or_404
from django.views.decorators.http import require_POST
from products.recommendations import Recommend

from products.models import Product
from .cart import Cart
from .forms import  AddProductToCartForm
from coupons.forms import CouponForm

@require_POST
def add_item_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddProductToCartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=['override'])
    return redirect('cart_detail')

@require_POST
def remove_item_from_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = AddProductToCartForm(
            initial={'quantity': item['quantity'],
                     'override':True}
        )
    coupon_form = CouponForm() #display coupon form 
    
    # Recommend products if only product(s) are in cart
    if cart:
        conn = Recommend()
        cart_products = [item['product'] for item in cart]
        recommended_products = conn.suggest_products_for(cart_products, max_results=4)
        return render(request, 'cart_detail.html', {'cart': cart, 'coupon_form':coupon_form,
                                                'recommended_products':recommended_products})
    return render(request, 'cart_detail.html', {'cart': cart, 'coupon_form':coupon_form,})
