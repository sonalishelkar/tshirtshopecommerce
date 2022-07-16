from ast import Expression
from multiprocessing import context
import traceback
from django.shortcuts import redirect, render, HttpResponse
from store.forms.authforms import CustomerCreationForm, CustomerAuthForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser, logout
from store.models import Tshirt, SizeVariant, Cart, Order, OrderItem, Payment, Occasion, Brand, Color, IdealFor, NeckType, Sleeve
from store.forms.checkout_form import CheckForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from urllib.parse import urlencode

def home(request):
    
    query = request.GET
    tshirts = []
    tshirts = Tshirt.objects.all()

    brand = query.get('brand')
    neckType = query.get('necktype')
    color = query.get('color')
    idealFor = query.get('idealfor')
    sleeve = query.get('sleeve')
    page = query.get('page')

    if (page is None or page == ''):
        page = 1

    if brand!='' and brand is not None:
        tshirts = tshirts.filter(brand__slug = brand)

    if neckType!='' and neckType is not None:
        tshirts = tshirts.filter(neck_type__slug = neckType)

    if color!='' and color is not None:
        tshirts = tshirts.filter(color__slug = color)

    if idealFor!='' and idealFor is not None:
        tshirts = tshirts.filter(ideal_for__slug = idealFor)

    if sleeve!='' and sleeve is not None:
        tshirts = tshirts.filter(sleeve__slug = sleeve)


    occasions = Occasion.objects.all()
    brands = Brand.objects.all()
    sleeves = Sleeve.objects.all()
    idealFor = IdealFor.objects.all()
    neckType = NeckType.objects.all()
    colors = Color.objects.all()

    print(request.user)
    
    cart = request.session.get('cart')
    print(cart)
    paginator = Paginator(tshirts, 6)
    page_object = paginator.get_page(page)

    query = request.GET.copy()
    query['page'] = ''
    pageurl = urlencode(query)
    context = {
        "page_object": page_object,
        "occasions" : occasions,
        "brands": brands,
        "colors" : colors,
        "sleeves": sleeves,
        "neckType" : neckType,
        "idealFor": idealFor,
        "pageurl" : pageurl
        }
    return render(request, template_name='store/home.html', context=context)
    
