from django.urls import path

from .views import create_order_view

urlpatterns = [
    path('', create_order_view, name='create_order'),
]
