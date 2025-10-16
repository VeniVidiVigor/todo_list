from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.tasks_index, name='tasks'),
    path('add_task', views.add_task, name='add_task'),
    path('toggle_status/<int:task_id>/', views.toggle_status, name='toggle_status'),
    path('add_new_task', views.add_new_task, name='add_new_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('tasks/', views.filter_status_tasks, name='filter_status_tasks'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register')
]