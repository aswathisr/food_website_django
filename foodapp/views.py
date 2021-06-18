from django.core.paginator import Paginator
from django.template.context_processors import request
from django.views.generic import ListView, DetailView

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.
from .models import Category


# def test(request):
#     items = Item.objects.all()
#     return render(request, 'index.html', {"items": items})
#
#
#
# def hello(request):
#         items = Item.objects.all()
#         return render(request, 'index.html', {"items": items})


def product_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    products=Product.objects.all()
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products=products.filter(category=category)

    else:
        products=Product.objects.all()

    return render(request,"index.html",{'categories':categories, 'category':category,'products':products})


def product_detail(request,category_slug,slug):
    products = Product.objects.get(category__slug=category_slug, slug=slug)
    return render(request, "product_detail.html", {'product': products})






