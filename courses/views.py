from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from core.models import Course
from .serializers import CourseSerializer


class ListCourses(ListCreateAPIView):
    """
        API View for listing and creating course models. UUID field preferred as a
        lookup_field for security purposes, but id of course model was used.
    """
    model = Course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # lookup_field = "uuid"


class DetailCourse(RetrieveDestroyAPIView):
    """
        API view for getting or deleting course model.
        Deleting Course model causes all related Contact and Branch models to be deleted to
    """
    model = Course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # lookup_field = "uuid"
