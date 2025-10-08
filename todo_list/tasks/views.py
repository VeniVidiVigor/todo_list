from django.shortcuts import render, get_object_or_404, redirect
from .models import Tasks


# Create your views here.
def add_task(request):
    return render(request, 'tasks/add_task.html')

def tasks_index(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

def toggle_status(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Tasks, id=task_id)
        # Меняем статус на противоположный
        task.completed = not task.completed
        task.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

def add_new_task(request):
    if request.method == 'POST':
        title = request.POST.get('title-task')
        description = request.POST.get('description-task')
        if title:  # Проверяем, что заголовок не пустой
            Tasks.objects.create(title=title, description=description)
    return redirect('tasks')

def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return redirect('tasks')

def edit_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title-task')
        description = request.POST.get('description-task')
        if title:  # Проверяем, что заголовок не пустой
            task.title = title
            task.description = description
            task.save()
            return redirect('tasks')
    return render(request, 'tasks/edit_task.html', {'task': task})
    
