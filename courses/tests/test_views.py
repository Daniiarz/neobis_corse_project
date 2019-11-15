from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient
from courses.serializers import CourseSerializer

from .utils import CourseFactory, fake, CategoryFactory
from core.models import Course

COURSES_URL = reverse("courses")


class TestCourseViews(TestCase):
    """
        Class for testing all courses views.
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.category = CategoryFactory(name="Course to be deleted")

    def test_get_course_list(self):
        """
            Testing GET method on course/ endpoint
        """
        CourseFactory(category=self.category)
        CourseFactory(category=self.category)
        response = self.client.get(COURSES_URL)

        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_course(self):
        """
            Testing POST method on course/ endpoint
        """
        payload = {
            "name": "English courses",
            "description": fake.paragraph(nb_sentences=1, variable_nb_sentences=True, ext_word_list=None),
            "logo": fake.file_path(),
            "category": self.category.id,
            "branches": [
                {
                    "longitude": fake.zipcode_plus4(),
                    "latitude": fake.zipcode_plus4(),
                    "address": fake.address()
                }
            ],
            "contacts": [
                {
                    "contact_type": 1,
                    "value": fake.phone_number()
                }
            ]
        }

        response = self.client.post(COURSES_URL, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        exists = Course.objects.filter(name=response.data["name"]).exists()
        self.assertTrue(exists)

    def test_course_detail_get(self):
        """
            Testing detail view GET method for course models on courses/{id} endpoint
        """
        course = CourseFactory(category=self.category)
        response = self.client.get(
            course.get_absolute_url()
        )

        serializer = CourseSerializer(course)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_course_detail_delete(self):
        """
            Testing detail view delete method for course models on courses/{id} endpoint
        """
        course = CourseFactory(category=self.category)
        response = self.client.delete(
            course.get_absolute_url()
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        exists = Course.objects.filter(name="Course to be deleted")
        self.assertFalse(exists)
