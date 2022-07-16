from ast import Expression
from multiprocessing import context
import traceback
from django.shortcuts import redirect, render, HttpResponse
from store.forms.authforms import CustomerCreationForm, CustomerAuthForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser, logout
from store.models import Tshirt, SizeVariant, Cart, Order, OrderItem, Payment, Occasion, Brand, Color, IdealFor, NeckType, Sleeve
from store.forms.checkout_form import CheckForm

from django.views.generic.list import ListView


#@login_required(login_url='/login/')
#def orders(request):
    #user = request.user
    #orders = Order.objects.filter(user = user).order_by('-date').exclude(orderStatus='PENDING')
    #context = {
       # "orders" : orders
    #}
   # return render(request, template_name='store/orders.html' , context=context)

class OrderListView(ListView):
    template_name = 'store/orders.html'
    model = Order
    paginate_by = 4
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user = self.request.user).order_by('-date').exclude(orderStatus='PENDING')   
