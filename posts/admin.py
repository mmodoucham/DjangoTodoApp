from django.contrib import admin

from posts.models import CreateTodo, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(CreateTodo)
