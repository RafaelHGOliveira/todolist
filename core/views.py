from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo
from .forms import TodoModelForm

class IndexView(CreateView, ListView):
    models = Todo
    template_name = 'index.html'
    queryset = Todo.objects.all().order_by('id')
    context_object_name = 'todos'
    fields = ['nome']
    success_url = reverse_lazy('index')
    

class UpdateTodoView(UpdateView):
    model = Todo
    template_name = 'todo_form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')

class DeleteTodoView(DeleteView):
    model = Todo
    template_name = 'todo_del.html'
    success_url = reverse_lazy('index')
