from django.contrib import admin

# Register your models here.

from .models import Topic, Lesson, Progress

admin.site.register(Topic)
admin.site.register(Lesson)
admin.site.register(Progress)
