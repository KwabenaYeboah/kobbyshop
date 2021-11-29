from django.shortcuts import render, redirect
from django.urls import reverse

from .models import OrderItem
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
                OrderItem.objects.create(customer=order, product=item['product'],
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