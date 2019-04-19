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

    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     slug = self.kwargs.get('slug')
    #     #instance = get_object_or_404(Product, slug=slug, active=True)
    #     # try:
    #     #     instance = Product.objects.get(slug=slug, active=True)
    #     # except Product.DoesNotExist:
    #     #     raise Http404("Not found..")
    #     # except Product.MultipleObjectsReturned:
    #     #     qs = Product.objects.filter(slug=slug, active=True)
    #     #     instance = qs.first()
    #     # except:
    #     #     raise Http404("Uhhhh")
    #     # return instance

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
        'queryset' : instance
    }
    return render(request, "products/detail.html", context)