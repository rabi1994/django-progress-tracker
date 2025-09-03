from rest_framework import serializers
from .models import Topic, Lesson, Progress

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "title", "order", "topic"]

class TopicSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Topic
        fields = ["id", "name", "description", "lessons"]

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ["id", "user", "lesson", "is_completed", "completed_at"]
        read_only_fields = ["completed_at"]
