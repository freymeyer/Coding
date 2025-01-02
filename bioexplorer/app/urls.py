from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("counter/", views.counter, name="Counter"),
    path("password/", views.Password,name="password")
]