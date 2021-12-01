from django.urls import path

from .views import apply_coupon_view
urlpatterns = [
    path('', apply_coupon_view, name='apply_coupon'),
]
