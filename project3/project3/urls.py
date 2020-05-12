"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from accounts.views import login_page, register_page, guest_register_view
from addresses.views import checkout_address_create_view,checkout_address_reuse_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_page, name='register'),
    path('register/guest', guest_register_view, name='guest_register'),
    path('checkout/address/create/',checkout_address_create_view,name='checkout_address_create'),
    path('checkout/address/reuse/',checkout_address_reuse_view,name='checkout_address_reuse'),
    path('',include('products.urls', namespace='products')),
    path('cart/',include('cart.urls' ,namespace='cart')),
]
