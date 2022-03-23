from django.shortcuts import render


# Create your views here.
def helloworld(request):
    name = 'Alex'
    context = {'name': name}
    return render(request, "helloworld/helloworld.html", context)


def hellostudent(request):
    return render(request, "helloworld/hellostudent.html",)
