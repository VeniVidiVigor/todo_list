from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def task_list(request):
    if request.method == "POST" and "name" in request.POST:
        if 'name' in request.POST:
            name = request.POST.get('name')
            if name:
                Task.objects.create(name=name)
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def toggle_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = not task.status
    task.save()
    return redirect('task_list')