from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = { 
        "title" : "Hello Home page"
    }
    return render(request, "home_page.html",context)

def about_page(request):
    return render(request,"Hello World About page")

def contact_page(request):
    return render(request,"Hello World Contact Page")