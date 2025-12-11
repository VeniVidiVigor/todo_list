from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseForbidden
from .models import Tasks
# from .forms import CustomRegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def add_task(request):
    return render(request, 'tasks/add_task.html')

@login_required
def tasks_index(request):
    tasks = Tasks.objects.filter(user=request.user)
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

@login_required
def toggle_status(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Tasks, id=task_id)
        if task.user != request.user:
            return HttpResponseForbidden("Это не ваша задача.")
        task.completed = not task.completed
        task.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def add_new_task(request):
    if request.method == 'POST':
        title = request.POST.get('title-task')
        description = request.POST.get('description-task')
        if title:  # Проверяем, что заголовок не пустой
            Tasks.objects.create(title=title, description=description, user=request.user)
    return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if task.user != request.user:
        return HttpResponseForbidden("Это не ваша задача.")
    if request.method == 'POST':
        task.delete()
    return redirect('tasks')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if task.user != request.user:
        return HttpResponseForbidden("Это не ваша задача.")
    if request.method == 'POST':
        title = request.POST.get('title-task')
        description = request.POST.get('description-task')
        if title:
            task.title = title
            task.description = description
            task.save()
            return redirect('tasks')
    return render(request, 'tasks/edit_task.html', {'task': task})

@login_required
def filter_status_tasks(request):
    completed = request.GET.get('status')
    if completed == 'completed':
        tasks = Tasks.objects.filter(user=request.user, completed=True)
    elif completed == 'active':
        tasks = Tasks.objects.filter(user=request.user, completed=False)
    else:
        tasks = Tasks.objects.filter(user=request.user)
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks,
        'filter_status': completed
    })

