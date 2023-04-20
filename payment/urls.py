from django.urls import path
from .views import payment_list, payment_detail

urlpatterns = [
    path('payments', payment_list, name='payment_list'),
    path('payments/<int:pk>', payment_detail, name='payment_detail'),
]
