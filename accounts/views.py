from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect('login') 
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('book_lessons')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})