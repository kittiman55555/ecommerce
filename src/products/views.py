from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product
from django.http import Http404
# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()
    tempalte_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context

def product_list_view(request):
    queryset = Product.objects.all()
    context = { 
        'object_list' : queryset
    }
    return render(request, "products/product_list.html", context)


def product_detail_view(request, pk=None, *args, **kwargs):
    #instance = Product.objects.get(pk=pk)
    #instance = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = get_object_or_404(Product, pk=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist")
    # except:
    #     print("huh ?")
    #instance = Product.objects.get_by_id(pk)
    qs = Product.objects.filter(id=pk)
    
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("Product doesn't exist")
    context = { 
        'object_list' : instance
    }
    return render(request, "products/detail.html", context)