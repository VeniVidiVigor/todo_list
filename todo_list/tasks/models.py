from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tasks(models.Model):
    title = models.CharField('Названия задачи', max_length=100)
    description = models.TextField('Описание задачи')
    completed = models.BooleanField("Завершенность задачи",default=False)
    created_at = models.DateTimeField("Когда создана задача",auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'