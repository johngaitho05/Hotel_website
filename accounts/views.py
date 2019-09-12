from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method=='POST':
        if request.POST['password'] == request.POST['password1']:
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request,'home.html', {'error': "That phone number has already been registered"})
            except User.DoesNotExist:
                User.objects.create_user(username=request.POST['email'],password=request.POST['password'],first_name=request.POST['fname'],last_name=request.POST['lname'])
                user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('homepage')
        else:
            return render(request, 'home.html', {'signup_error': "Passwords not matching"})


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'home.html',{'login_error':'Invalid credentials. Try again'})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('homepage')
