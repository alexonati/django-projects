from django.shortcuts import render

# Create your views here.
def todoview(request):
    return render(request, "todoapp/homepage.html")
