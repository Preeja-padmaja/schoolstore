from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def school_fun(request):
    return render(request,'index.html')
def login_fun(request):
    if request.method == 'POST':
        u_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=u_name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/user_page')
        else:
            messages.info(request, "INVALID CREDENTIALS")
            return redirect('/login')
    return render(request, 'login.html')
def register_fun(request):
    if request.method == 'POST':
        u_name = request.POST['user_name']
        password = request.POST['password']
        c_password = request.POST['c_password']
        if password == c_password:
            if User.objects.filter(username=u_name).exists():
                messages.info(request,"User Name Already Exists")
                return redirect('/register')
            else:
                user = User.objects.create_user(password=password,username=u_name)
                user.save()
                return redirect('/login')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('/register')
            return redirect('/index')
    return render(request, 'register.html')
def logout_fun(request):
    auth.logout(request)
    return redirect('/login')
def user_fun(request):
    if request.method == 'POST':
        messages.info(request, "Order Confirmed")
    return render(request, 'user_page.html')