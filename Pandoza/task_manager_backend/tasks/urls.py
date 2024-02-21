from .views import TasksView
from django.urls import path

urlpatterns = [
    path('tasks/', TasksView.as_view()),
]