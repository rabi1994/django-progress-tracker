from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Topic, Lesson, Progress
from .serializers import TopicSerializer, LessonSerializer, ProgressSerializer
from django.utils.timezone import now

class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.prefetch_related("lessons").all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticated]

class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"])
    def toggle(self, request, pk=None):
        prog = self.get_object()
        prog.is_completed = not prog.is_completed
        prog.completed_at = now() if prog.is_completed else None
        prog.save(update_fields=["is_completed", "completed_at"])
        return Response(ProgressSerializer(prog).data, status=status.OK)
