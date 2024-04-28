from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from tasks.models import Task

from tasks.form import TaskForm


class TasksListView(ListView):
    template_name = "tasks/tasks-view.html"
    context_object_name = "tasks"
    queryset = Task.objects.filter(archived=False)


class TaskDetailView(DetailView):
    template_name = "tasks/task-detail.html"
    context_object_name = "task"
    model = Task


class TaskCreateView(CreateView):
    model = Task
    template_name = "tasks/task-create.html"
    fields = 'title', 'description', 'cost'
    success_url = reverse_lazy("tasks:tasks_list")


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "tasks/task-update.html"
    form_class = TaskForm

    def get_success_url(self):
        return reverse("tasks:task_detail", kwargs={"pk": self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:tasks_list")

    def form_valid(self, form):
        success_url = super().get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)
