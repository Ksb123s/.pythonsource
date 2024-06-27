from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/photo/
    path("", views.list, name="photo_list"),
    # http://127.0.0.1:8000/photo/create/
    path("", views.create, name="photo_create"),
]
