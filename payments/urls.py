from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import process_payment_view, payment_cancelled_view, payment_done_view

urlpatterns = [
    path(_('process/'), process_payment_view, name='payment_process'),
    path(_('done/'),  payment_done_view, name='payment_done'),
    path(_('cancelled/'),  payment_cancelled_view, name='payment_cancelled'),
]
