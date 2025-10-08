from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_index, name='tasks_home'),
    path('add_task', views.add_task, name='add_task'),
    path('toggle_status/<int:task_id>/', views.toggle_status, name='toggle_status'),
    path('add_new_task', views.add_new_task, name='add_new_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task')
]