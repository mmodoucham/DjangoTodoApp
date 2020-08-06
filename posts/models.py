from django.db import models


# Create your models here.
from django.http import HttpResponseRedirect
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class CreateTodo(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

