from django.urls import path

from .views import add_item_to_cart_view, remove_item_from_cart_view, cart_detail_view

urlpatterns = [
    path('', cart_detail_view, name='cart_detail'),
    path('add/<int:product_id>/', add_item_to_cart_view, name='cart_add_item'),
    path('remove/<int:product_id>/', remove_item_from_cart_view, name='cart_remove_item'),
]
