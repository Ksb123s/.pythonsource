from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = "blog"


urlpatterns = [
    # ex http://127.0.0.1:8000/blog/
    path("",views.list,name="list"),
    # ex http://127.0.0.1:8000/blog/post/1/
    path("post/<int:post_id>/",views.detail,name="detail"),
    # ex http://127.0.0.1:8000/blog/post/create/
    path("post/create/",views.create,name="create"),
    # ex http://127.0.0.1:8000/blog/post/modify/1/
    path("post/modify/<int:post_id>/",views.modify,name="modify"),
    # ex http://127.0.0.1:8000/blog/post/delete/1/
    path("post/delete/<int:post_id>/",views.delete,name="delete"),
]