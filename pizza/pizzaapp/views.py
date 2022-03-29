from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import PizzaModel, CustomerModel, OrderModel


# Create your views here.
def adminloginview(request):
    return render(request, "pizzaapp/adminlogin.html")


def authenticatedadmin(request):
    username_entered_by_user = request.POST['username']
    password_entered_by_user = request.POST['password']

    user = authenticate(username=username_entered_by_user, password=password_entered_by_user)

    if user is not None and user.username == "admin":
        login(request, user)
        return redirect('adminhomepage')
    if user is None:
        messages.add_message(request, messages.ERROR, "Invalid credentials...please retry.")
        return redirect('adminloginpage')


def adminhomepageview(request):
    username_of_admin = request.user.username
    context = {"pizzas": PizzaModel.objects.all(),'username':username_of_admin}
    return render(request, "pizzaapp/adminhomepage.html", context)


def logoutadmin(request):
    logout(request)
    return redirect('homepageview')


def addpizza(request):
    name = request.POST['pizza']
    price = request.POST['price']
    PizzaModel(name=name, price=price).save()
    return redirect('adminhomepage')


def deletepizza(request, pizzapk):
    PizzaModel.objects.filter(id=pizzapk).delete()
    return redirect('adminhomepage')


def homepageview(request):
    return render(request, "pizzaapp/homepage.html")


def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneno = request.POST['phone']
    if User.objects.filter(username=username).exists():
        messages.add_message(request, messages.ERROR,"User already exists. Please login.")
        return redirect('homepageview')
    User.objects.create_user(username=username, password=password).save()
    last_object_id_in_db = len(User.objects.all())-1
    CustomerModel(userid = User.objects.all()[int(last_object_id_in_db)].id, phoneno = phoneno).save()
    messages.add_message(request, messages.ERROR, "User created. Please login.")
    return redirect('homepageview')


def userloginview(request):
    return render(request, "pizzaapp/userlogin.html")

def authenticate_user(request):
    username_entered_by_user = request.POST['username']
    password_entered_by_user = request.POST['password']

    user = authenticate(username=username_entered_by_user, password=password_entered_by_user)

    if user is not None:
        login(request, user)
        return redirect('customerpage')
    if user is None:
        messages.add_message(request, messages.ERROR, "Invalid credentials...please retry or create an account.")
        return redirect('userloginpage')

def customerview(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')
    username = request.user.username
    context = {"username":username, 'pizzas': PizzaModel.objects.all()}
    return render(request, "pizzaapp/customerpage.html",context)

def userlogout(request):
    logout(request)
    return redirect('homepageview')

def placeorders(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')
    username = request.user.username
    phone_number = CustomerModel.objects.filter(userid = request.user.id)[0].phoneno
    delivery_address = request.POST['address']

    for pizza in PizzaModel.objects.all():
        pizzaid = pizza.id
        name = pizza.name
        price = pizza.price
        quantity = request.POST.get(str(pizzaid)," ")
        ordered_items = ""
        if str(quantity) != "0" and str(quantity) == " ":
            ordered_items = ordered_items + name + " " + str(int(quantity)*int(price)) + " " +"quantity: " + quantity + "   "

    OrderModel(username=username, phone_number=phone_number, address=delivery_address, order_items=ordered_items).save()
    messages.add_message(request,messages.SUCCESS,"The order has been successfully placed.")
    return redirect('customerpage')

def userorders(request):
    orders = OrderModel.objects.filter(username = request.user.username)
    context = {'orders': orders}
    return render(request,'pizzaapp/userorders.html',context)

def allorders(request):
    orders_all = OrderModel.objects.all()
    context = {'orders': orders_all}
    return render(request,'pizzaapp/adminorders.html', context)

def acceptorder(request, orderpk):
    order = OrderModel.objects.filter(id = orderpk)[0]
    order.status = "accepted"
    order.save()
    return redirect(request.META['HTTP_REFERER'])

def declineorder(request, orderpk):
    order = OrderModel.objects.filter(id = orderpk)[0]
    order.status = "declined"
    order.save()
    return redirect(request.META['HTTP_REFERER'])