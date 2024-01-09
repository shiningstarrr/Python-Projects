from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Task,Todo
# Create your views here.

def home(request):
    return render(request, 'home.html')

# def detail(request):
#     tasks = Task.objects.all()
#     context={
#         'tasks':tasks,
#     }
#     return render(request, 'detail.html', context)

def todos(request):
    todos = Todo.objects.filter(is_completed=False).order_by('-updated_at')
    finished=Todo.objects.filter(is_completed=True)
    context={
        'todo':todos,
        'finished':finished,
    }
    return render(request, 'detail.html', context)

def addTask(request):
    task = request.POST['task']
    Todo.objects.create(task=task, is_completed=False)
    return redirect('detail')

def markDone(request,id):
    task = get_object_or_404(Todo, id=id)
    task.is_completed = True
    task.save()
    return redirect('detail')

def remove(request, id):
    task = get_object_or_404(Todo,id=id)
    task.is_completed = False
    task.save()
    return redirect('detail')

def deleteTask(request, id):
    task = get_object_or_404(Todo,id=id)
    task.delete()
    return redirect('detail')

def edit_task(request, id):
    get_task=get_object_or_404(Todo,id=id)
    if request.method == 'POST': # update button will send post request to server
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('detail')
    else:
        context={
            'get_task':get_task,
        }
    
    return render(request,'editTask.html', context)