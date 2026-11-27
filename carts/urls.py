from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/',views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/',views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/',views.remove_cart_item, name='remove_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    # path('update_cart/', views.update_cart, name='update_cart'),
    # path('update_cart_item/', views.update_cart_item, name='update_cart_item'),
    # path('order_detail/<int:order_id>/', views.order_detail,name='order_detail'),
    # path('order_complete/', views.order_complete, name='order_complete'),
    # path('payment/<int:order>/', views.payment, name='payment'),
    

]