from django.urls import path
from user.views import user_list, user_detail

urlpatterns = [
    path('users', user_list, name='user_list'),
    path('users/<int:pk>', user_detail, name='user_detail'),
]