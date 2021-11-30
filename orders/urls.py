from django.urls import path

from .views import create_order_view, order_detail_view

urlpatterns = [
    path('admin/order/<int:order_id>/', order_detail_view, name='admin_order_detail'),
    path('', create_order_view, name='create_order'),
]
