from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


def login_check(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(username)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            user_exists = "false"
            return render(request, 'log_in.html', {'user_exists': user_exists})
    else:
        user_exists = True
        return render(request, 'log_in.html', {'user_exists': user_exists})

def sign_up(request):
    user_exists = False

    if request.method == 'POST':
        usernameInput = request.POST['username']
        passwordInput = request.POST['password']

        if User.objects.filter(username=usernameInput).exists():
            user_exists = True
        else:
            User.objects.create_user(username=usernameInput, password=passwordInput)
            return redirect('login')

    return render(request, 'sign_up.html', {'user_exists': user_exists})


def welcome(request):
    return render(request, 'welcome.html')
