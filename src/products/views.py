from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product
from django.http import Http404
# Create your views here.

class ProductListView(ListView):
    #queryset = Product.objects.all()
    tempalte_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     return context

class ProductFeaturedListView(ListView):
    tempalte_name = "products/featured-list.html"
 
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    tempalte_name = "products/featured-detail.html"
                            
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/detail.html"

    def get_objects(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('slug')
        instance = Product.objects.get_queryset(pk)
        if instance is None:
            raise Http404("product doesn't exist")
        return instance

def product_list_view(request):
    queryset = Product.objects.all()
    context = { 
        'object_list' : queryset
    }
    return render(request, "products/product_list.html", context)


def product_detail_view(request, pk=None, *args, **kwargs):
    instance = Product.objects.get_by_id(pk)
    print(instance)
    if instance is None:
        raise Http404("Product doesn't exist")

    # qs = Product.objects.filter(id=pk)
    
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")
    context = { 
        'object_list' : instance
    }
    return render(request, "products/detail.html", context)