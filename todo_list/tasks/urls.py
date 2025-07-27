from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('toggle_status/<int:task_id>/', views.toggle_status, name='toggle_status'),
]
