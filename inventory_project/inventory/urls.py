from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:id>/', views.update_product, name='update_product'),
    path('order/', views.create_order, name='create_order'),
    path('orders/', views.order_list, name='order_list'),
    path('update-order/<int:id>/', views.update_order, name='update_order'),
    path('dashboard/',views.dashboard,name='dashboard'),
]