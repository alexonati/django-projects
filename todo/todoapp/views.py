from django.shortcuts import render, redirect
from .models import TodoModel

# Create your views here.
def todoview(request):
    my_todo = TodoModel.objects.all()
    context = {'my_todos': my_todo}
    return render(request, "todoapp/homepage.html", context)

def addtask(request):
    mytask = request.POST['task']
    TodoModel(task = mytask).save()
    return redirect(request.META['HTTP_REFERER'])