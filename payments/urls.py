from django.urls import path

from .views import process_payment_view, payment_cancelled_view, payment_done_view

urlpatterns = [
    path('process/', process_payment_view, name='payment_process'),
    path('done/', payment_done_view, name='payment_done'),
    path('cancelled/', payment_cancelled_view, name='payment_cancelled'),
]
