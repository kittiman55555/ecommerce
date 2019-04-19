"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from products.views import (
    product_list_view, 
    ProductListView, 
    product_detail_view,
    ProductFeaturedListView,
    ProductFeaturedDetailView
)
from .view import home_page, login_page, register_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page , name='home_page'), 
    #path('products/',ProductListView.as_view() , name='product_list_view'), 
    path('products/',product_list_view , name='product_list_view'), 
    path('featured/',ProductFeaturedListView.as_view() , name='product_list_view'), 
    path('featured/<int:pk>',ProductFeaturedDetailView.as_view() , name='product_detail_view'),
    path('products/<int:pk>',product_detail_view , name='product_detail_view'),
    path('login/',login_page , name='login_page'),
    path('register/',register_page , name='register_page'),
]

if settings.DEBUG: 
    urlpatterns =  urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns =  urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)