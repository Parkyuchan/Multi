from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request) :
    return render(request, 'home.html')
 
 
def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.email))
 
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            accounts = authenticate(email=email, password=raw_password)
            login(request, accounts)
            destination = kwargs.get("next")
            #destination = get_redirect_if_exists(request)
            if destination: # if destination != None
                return redirect(destination)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
 
    return render(request, 'register.html', context)
 
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('home')
 

def login_view(request, *args, **kwargs):
    context = {}
 
    user = request.user
    if user.is_authenticated:
        return redirect('home')
 
    destination = get_redirect_if_exists(request)
    if request.POST:
        form = AccountAuthForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                if destination:
                    return redirect(destination)
                return redirect('home')
    else:
        form = AccountAuthForm()
 
    context['login_form'] = form
 
    return render(request, 'login.html', context)
 
 
def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect