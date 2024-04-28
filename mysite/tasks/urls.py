from django.urls import path
from tasks import views

app_name = "tasks"

urlpatterns = [
    path('tasks-list/', views.TasksListView.as_view(), name='tasks_list'),
    path('task/detail/<int:pk>', views.TaskDetailView.as_view(), name="task_detail"),
    path('task/upadate/<int:pk>', views.TaskUpdateView.as_view(), name="task_update"),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name="task_delete"),
    path('task/create', views.TaskCreateView.as_view(), name="task_create"),
]
