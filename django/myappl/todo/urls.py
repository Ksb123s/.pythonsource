from django.urls import path
from . import views
urlpatterns = [
    path("",views.list, name="list"),
    path("create/",views.create, name="create"),
    path("<int:id>/",views.read, name="read"),
    path("done/<int:id>/",views.done, name="done"),
    path("done_list/",views.done_list, name="done_list"),
    path("edit/<int:id>/",views.edit, name="edit"),
]
