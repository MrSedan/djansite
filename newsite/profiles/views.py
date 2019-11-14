from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    return render(request, 'profiles/index.html')

def log_in(request):
    if request.user.is_authenticated:
        messages.success(request, "Вы уже вошли!")
        return redirect('profile:index')
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Успешный вход!")
                    return redirect('profile:index')
            else:
                messages.error(request, "Неправильные логин или пароль!")
    form = LoginForm()
    return render(request, 'profiles/login.html', {'form':form})

def log_out(request):
    if request.user.is_anonymous:
        return redirect('profile:index')
    logout(request)
    messages.success(request, "Вы успешно вышли из аккаунта!")
    return redirect('profile:index')

def register(request):
    if request.user.is_authenticated:
        messages.success(request, "Вы уже вошли!")
        return redirect('profile:index')
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            try:
                User.objects.get(username=form.cleaned_data['login'])
                messages.error(request, "Такой ник уже зарегистрирован!")
                form = RegisterForm()
                return redirect('profile:register', kwargs={'form': form})
            except:
                pass

            try:
                User.objects.get(email=form.cleaned_data['email'])
                messages.error(request, "Эта почта уже зарегистрирована!")
                form = RegisterForm()
                return redirect('profile:register', kwargs={'form': form})
            except:
                pass
            email = form.cleaned_data['email']
            if form.cleaned_data['password'] != form.cleaned_data['re_password']:
                messages.error(request, "Пароли не совпадают!")
                form = RegisterForm()
                return redirect('profile:register', kwargs={'form': form})
            else:
                user = User(first_name=first_name, email=email, username=request.POST['login'])
                if second_name is not None:
                    user.last_name = second_name
                user.set_password(form.cleaned_data['password'])
                user.save()
                messages.success(request, "Вы успешно зарегистрировались!")
                form = LoginForm()
                return redirect('profile:login')
    form = RegisterForm()
    return render(request, 'profiles/register.html', {'form': form})
    
