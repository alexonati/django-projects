from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def adminloginview(request):
    return render(request, "pizzaapp/adminlogin.html")

def authenticatedadmin(request):
    username_entered_by_user = request.POST['username']
    password_entered_by_user = request.POST['password']

    user = authenticate(username=username_entered_by_user, password=password_entered_by_user)

    if user is not None and user.username=="admin":
        login(request, user)
        return redirect('adminhomepage')
    if user is None:
        messages.add_message(request, messages.ERROR, "Invalid credentials...please retry.")
        return redirect('adminloginpage')

def adminhomepageview(request):
        return render(request, "pizzaapp/adminhomepage.html")

def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')