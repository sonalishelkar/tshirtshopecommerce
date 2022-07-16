from ast import Expression
from multiprocessing import context
import traceback
from django.shortcuts import redirect, render, HttpResponse
from requests import request
from store.forms.authforms import CustomerCreationForm, CustomerAuthForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser, logout
from store.models import Tshirt, SizeVariant, Cart, Order, OrderItem, Payment, Occasion, Brand, Color, IdealFor, NeckType, Sleeve, tshirt
from store.forms.checkout_form import CheckForm
from django.contrib.auth.decorators import login_required
from math import floor
from django.views.generic.detail import DetailView


class ProductDetailView(DetailView):
    template_name= 'store/product_details.html'
    model = Tshirt
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tshirt = context.get('tshirt')
        request = self.request
        
        size = request.GET.get('size')

        if size is None:
            size = tshirt.sizevariant_set.all().order_by('price').first()
        else:
            size = tshirt.sizevariant_set.get(size=size)

        size_price = floor(size.price)
        sell_price = size_price - (size_price * (tshirt.discount/100))
        sell_price = floor(size_price)
        context = {'tshirt': tshirt, 'price': size_price,
                'sell_price': sell_price, 'active_size': size}
        return context


