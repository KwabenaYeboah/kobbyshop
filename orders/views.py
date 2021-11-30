from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse

from .models import OrderItem, Order 
from .forms import CustomerOrderForm
from cart.cart import Cart
from .tasks import created_order

def create_order_view(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CustomerOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
            cart.clear()
            # Launch asynchronous task 
            created_order.delay(order.id)
            # Set order id into session
            request.session['order_id'] = order.id
            #redirect user for payment
            return redirect(reverse('payment_process'))
    form = CustomerOrderForm()
    return render(request, 'order.html', {'cart':cart, 'form':form})

@staff_member_required
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/order_detail.html', {'order':order})