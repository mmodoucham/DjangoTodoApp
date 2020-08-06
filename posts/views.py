# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView

from .models import *


class TodoView(ListView):
    template_name = 'base.html'
    context_object_name = 'todos'
    model = CreateTodo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateTodoView(CreateView):
    model = CreateTodo
    template_name = 'create.html'
    fields = ['title', 'desc', 'category', 'status']


class TodoUpdateView(UpdateView):
    model = CreateTodo
    template_name = 'update.html'
    fields = ['title', 'desc', 'category', 'status']


def delete_view(request, id):
    post = get_object_or_404(CreateTodo, id=id)
    post.delete()
    return redirect('/')
