from django.contrib import admin
from .models import Topic, Lesson, Progress


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "topic", "order")
    list_filter = ("topic",)
    search_fields = ("title",)


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "lesson", "is_completed", "completed_at")
    list_filter = ("is_completed", "completed_at", "lesson__topic")
    search_fields = ("user__username", "lesson__title")
