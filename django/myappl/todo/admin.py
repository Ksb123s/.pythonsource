from django.contrib import admin
from .models import Todo

# Register your models here.
# 어드민 사이트에서 관리할 모델 등록
admin.site.register(Todo)