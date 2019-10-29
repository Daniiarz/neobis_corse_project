from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^courses/$',
        view=views.ListCourses.as_view(),
        name='course_api'
    ),
    re_path(
        r'^courses/(?P<uuid>[-\w]+)/$',
        view=views.DetailCourse.as_view(),
        name="course_api"
    )
]
