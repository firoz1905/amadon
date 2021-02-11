from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('order_process/',views.order_process),
    path('checkout/', views.checkout)
]
