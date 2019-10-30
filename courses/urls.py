from django.urls import path
from . import views

urlpatterns = [
    path(
        'courses/',
        view=views.ListCourses.as_view(),
        name='courses'
    ),
    path(
        'courses/<int:pk>/',
        view=views.DetailCourse.as_view(),
        name="course-detail"
    )
]
