"""Tshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from store.views import  ProductDetailView, OrderListView,checkout, add_to_cart, home, cart, LoginView, signup, signout, validatePayment
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', home, name='homepage'),
    path('cart/', cart),
    path('orders/',login_required(OrderListView.as_view(), login_url='/login/'), name='orders'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', signup),
    path('logout/', signout),
    path('checkout/', checkout),
    path('product/<str:slug>', ProductDetailView.as_view()),
    path('addtocart/<str:slug>/<str:size>', add_to_cart),
    path('validate_payment', validatePayment),

]
