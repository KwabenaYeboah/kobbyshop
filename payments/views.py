from braintree import client_token, payment_method, payment_method_nonce
from django.shortcuts import render, redirect, get_object_or_404
import braintree
from django.conf import settings
from orders.models import Order

# instantiating Braintree payment gateway
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def process_payment_view(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    
    if request.method == 'POST':
        # let's get the 'nonce'
        nonce = request.POST.get('payment_method_nonce', None)
        # let's create and submit transaction
        payment = gateway.transaction.sale({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce': nonce,
            'options': { 'submit_for_settlement': True}
        })
        if payment.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction
            order.braintree_id = payment.transaction.id
            order.save()
            return redirect('payment_done')
        else:
            return redirect('payment_cancelled')
    else:
        # let's generate a token
        client_token = gateway.client_token.generate()
        return render(request, 'payments/payment_process.html',
                      {'order':order, 'client_token':client_token})

def payment_done_view(request):
    return render(request, 'payments/payment_done.html')

def payment_cancelled_view(request):
    return render(request, 'payments/cancelled.html')