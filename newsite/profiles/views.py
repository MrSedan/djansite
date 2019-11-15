from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from hashlib import md5
from django.contrib.auth.models import User
from .models import Info

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
            email = form.cleaned_data['email']
            try:
                User.objects.get(username=form.cleaned_data['login'].lower())
                messages.error(request, "Такой ник уже зарегистрирован!")
                form = RegisterForm()
                return redirect('profile:register', kwargs={'form': form})
            except:
                pass
            
            try:
                User.objects.get(email=email.lower())
                messages.error(request, "Эта почта уже зарегистрирована!")
                form = RegisterForm()
                return redirect('profile:register', kwargs={'form': form})
            except:
                pass
            if request.POST['password'] != request.POST['re_password']:
                messages.error(request, "Пароли не совпадают!")
                form = RegisterForm()
                return redirect('profile:register', kwargs={'form': form})
            else:
                user = User(first_name=first_name, email=email, username=request.POST['login'])
                if second_name is not None:
                    user.last_name = second_name
                user.set_password(request.POST['password'])
                user.save()
                info = Info(user=user, url=request.POST['login'].lower())
                info.save()
                messages.success(request, "Вы успешно зарегистрировались!")
                form = LoginForm()
                return redirect('profile:login')
    form = RegisterForm()
    return render(request, 'profiles/register.html', {'form': form})
    
def profile(request, s):
    try:
        info = Info.objects.get(url=s.lower())
        user = info.user
    except:
        return render(request, '404.html', {'text': "Этого пользователя не существует!"})
    digest = md5(user.email.lower().encode('utf-8')).hexdigest()
    return render(request, 'profiles/profile.html', {'user': user, 'avatar': digest})

def edit_profile(request):
    if request.method=='POST':
        url = request.POST['url']
        about = request.POST['about']
        try:
            info = Info.objects.get(user=request.user)
        except:
            return render(request, '404.html')
        urls = Info.objects.filter(url=url.lower()).first()
        if urls is not None:
            if urls.user != request.user:
                messages.error(request, "Такая ссылка уже зарезервирована!")
                return render(request, 'profiles/edit_profile.html', {'info':info})   
        info.url = url
        info.about = about
        info.save()
        messages.success(request, "Успешное изменение!")
        return redirect('profile:profile', url)
            
    if request.user.is_authenticated:
            try:
                info = Info.objects.get(user=request.user)
            except:
                return render(request, '404.html')
            return render(request, 'profiles/edit_profile.html', {'info':info})   
