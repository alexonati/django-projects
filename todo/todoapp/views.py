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

def deletetask(request, taskpk):
    TodoModel.objects.filter(id = taskpk).delete()
    return redirect(request.META['HTTP_REFERER'])

def edittaskview(request, taskpk):
    context = {'todopk': taskpk}
    return render(request,"todoapp/edit.html", context)

def edittask(request, taskpk):
   user_edited_task = request.POST['task']
   todo = TodoModel.objects.filter(id = taskpk)[0]
   todo.task = user_edited_task
   todo.save()
   return redirect('homepage')
