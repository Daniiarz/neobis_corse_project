from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from core.models import Course
from .serializers import CourseSerializer


class ListCourses(ListCreateAPIView):
    model = Course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "uuid"


class DetailCourse(RetrieveAPIView):
    model = Course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "uuid"

