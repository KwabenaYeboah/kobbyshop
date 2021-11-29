from celery import task
from django.core.mail import send_mail

from .models import Customer

@task
def created_order(order_id):
    '''A celery task to notify customers via email after an order is placed '''
    order = Customer.objects.get(id=order_id)
    subject = f'Order Number. {order.id}'
    message = f'Hello {order.first_name}, \n\n'\
              f'You have successfully placed an order.\nYour order ID is: {order.id}'
    mail_sent = send_mail(subject, message, 'orders@kobbyshop.com', [order.email])
    
    return mail_sent