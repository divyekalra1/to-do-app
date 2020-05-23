from django.contrib import admin
from django.urls import path
from .views import task_view, update_task_view, delete_task_view
urlpatterns = [
                    path("", task_view, name = "task_view"),
                    path("update/<str:key>", update_task_view, name = "update_task"),
                    path("delete/<str:key>", delete_task_view, name = "delete_task"),

              ]
