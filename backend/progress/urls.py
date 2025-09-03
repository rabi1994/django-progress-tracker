from rest_framework.routers import DefaultRouter
from .views import TopicViewSet, LessonViewSet, ProgressViewSet

router = DefaultRouter()
router.register(r"topics", TopicViewSet, basename="topic")
router.register(r"lessons", LessonViewSet, basename="lesson")
router.register(r"progress", ProgressViewSet, basename="progress")

urlpatterns = router.urls
