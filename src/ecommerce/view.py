from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth.models import User

def home_page(request):
    context = { 
        "title" : "Hello Home page"
    }
    return render(request, "home_page.html",context)

def contact_page(request):
    context = { 
        "title" : "Hello Contact page"
    }
    return render(request, "contact/view.html",context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = { 
        "form" : form
    }
    context['form'] = LoginForm()
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #print(request.user.is_authenticated())
            print(user)
            print("You are login")
            login(request, user)
            #redirect to sucess page
            #context['form'] = LoginForm()
            
            return redirect("/")
        else:
            print("Error")
    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = { 
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        print(form.cleaned_data)
        new_user= User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "auth/register.html", context)
