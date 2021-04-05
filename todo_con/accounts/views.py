from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def userLogin(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı!')

    return render(request, 'login.html', {'form': form})


def userRegister(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Kayıt Başarılı!')
        return redirect('login')
    return render(request, 'register.html', {'form': form})

login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')