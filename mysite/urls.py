from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coupon/', include('coupons.urls')),
    path('payment/', include('payments.urls')),
    path('order/', include('orders.urls')),
    path('cart/', include('cart.urls')),
    path('products/', include('products.urls')),   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)