from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import create_order_view, order_detail_view, generate_order_pdf_view

urlpatterns = [
    path('admin/order/<int:order_id>/', order_detail_view, name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/', generate_order_pdf_view, name='generate_order_pdf'),
    path(_(''), create_order_view, name='create_order'),
]
