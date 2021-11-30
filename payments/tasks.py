import weasyprint
from io import BytesIO
from celery import task
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order

@task
def payment_completed(order_id):
    '''
    Task to send an e-mail notifications when an order is successfully created
    '''
    order = Order.objects.get(id=order_id)
    
    #create email for invoice
    email_subject = f'Kobby Shop - Invoice no: {order.id}'
    email_message = f'Please, find attached the invoice for your purchase'
    email = EmailMessage(email_subject, email_message, 'payment@Kobbyshop.com', [order.email])
    
    # Generate PDF
    html = render_to_string('pdf.html', {'order':order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + '/css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    
    # Attach PDF
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    
    email.send()