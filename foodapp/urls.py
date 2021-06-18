from django.contrib import admin
from django.urls import path, include

from . import views
app_name='foodapp'


urlpatterns = [
    path('', views.product_list,name="product_list"),
    path('<slug:category_slug>', views.product_list,name="products_by_category"),
    path('<slug:category_slug>/<slug:slug>/',views.product_detail,name='product_detail')
    # path('hello', views.hello,name="hello"),

]

