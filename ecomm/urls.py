from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls')),
    path('order/', include('order.urls')),
    path('payment/', include('payment.urls')),
    path('product/', include('product.urls')),
    path('user/', include('user.urls')),
]
