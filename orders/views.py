
import weasyprint
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse

from .models import OrderItem, Order 
from .forms import OrderForm
from cart.cart import Cart
from .tasks import created_order

def create_order_view(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
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
    form = OrderForm()
    return render(request, 'order.html', {'cart':cart, 'form':form})

@staff_member_required
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/order_detail.html', {'order':order})

@staff_member_required
def generate_order_pdf_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('pdf.html', {'order':order})
    response = HttpResponse(content_type='application/pdf')
    response ['Content-Dispositon'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(
        settings.STATIC_ROOT + '/css/pdf.css')])
    return response