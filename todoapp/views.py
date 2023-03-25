from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from todoapp.models import Todo


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('list')


class TodoUpdateView(UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('list')


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('list')


def set_done(request, pk: int):
    todo = get_object_or_404(Todo, pk=pk)

    todo.done = True
    todo.save()

    return redirect('list')


def unset_done(request, pk: int):
    todo = get_object_or_404(Todo, pk=pk)

    todo.done = False
    todo.save()

    return redirect('list')
