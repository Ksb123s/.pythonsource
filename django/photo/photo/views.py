from django.shortcuts import render
from .models import Photo


def create(request):

    return render(request, "photo/photo_create.html")


def list(request):
    photos = Photo.objects.all()

    return render(request, "photo/photo_list.html", {"photos": photos})
