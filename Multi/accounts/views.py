from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm
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
            #login(request, accounts)
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
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/accounts')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'login.html')

'''def login_view(request, *args, **kwargs):
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
                auth.login(request, user)
                return redirect('/accounts')
                #login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                if destination:
                    return redirect(destination)
                return redirect('home')
    else:
        form = AccountAuthForm()
 
    context['login_form'] = form
 
    return render(request, 'login.html', context)'''
 
 
def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect