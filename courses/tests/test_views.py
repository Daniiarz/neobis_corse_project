from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient


class TestCourseViews(TestCase):
    """
        Class for testing all courses views.
    """

    def setUp(self) -> None:
        self.client = APIClient()

