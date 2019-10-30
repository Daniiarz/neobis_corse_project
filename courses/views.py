from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from core.models import Course
from .serializers import CourseSerializer


class ListCourses(ListCreateAPIView):
    """
        API View for listing and creating course models. UUID field preferred as a
        lookup_field for security purposes, but i was forced to use id of model as lookup field.
    """
    model = Course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # lookup_field = "uuid"


class DetailCourse(RetrieveDestroyAPIView):
    """
        API view for getting or deleting course model
    """
    model = Course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # lookup_field = "uuid"
