from django.shortcuts import render, redirect
from .models import CounterModel


# Create your views here.

def counter(request):
    number = CounterModel.objects.filter(id=1)[0]
    number = number.number
    context = {'number': number}
    return render(request, "counter/counter.html", context)


def increment(request):
    number = CounterModel.objects.filter(id=1)[0]
    number.number = int(number.number) + 1
    number.save()
    return redirect(request.META['HTTP_REFERER'])


def decrement(request):
    number = CounterModel.objects.filter(id=1)[0]
    number.number = int(number.number) - 1
    number.save()
    return redirect(request.META['HTTP_REFERER'])


def reset(request):
    number = CounterModel.objects.filter(id=1)[0]
    number.number = 0
    number.save()
    return redirect(request.META['HTTP_REFERER'])
