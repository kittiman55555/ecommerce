from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
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
