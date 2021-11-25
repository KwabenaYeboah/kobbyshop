from django.urls import path

from .views import product_list_view, product_detail_view

urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('<slug:category_slug>/', product_list_view, name='product_list_by_category'),
    path('<slug:slug>/<int:pk>/', product_detail_view, name='product_detail'),   
]
