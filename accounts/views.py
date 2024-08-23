from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('booking:booking_home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('login') 