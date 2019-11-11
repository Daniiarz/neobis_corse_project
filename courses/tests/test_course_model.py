from django.test import TestCase
from django.db.utils import IntegrityError

from rest_framework.test import APIClient
from rest_framework import status

from . import utils


class TestModels(TestCase):
    """
        Class for testing Course model
    """

    def setUp(self) -> None:
        self.category = utils.CategoryFactory()

    def test_create_course_model(self):
        """
            Test that course object can be created and belongs to specific category.
            Also, test str method works correctly
        """
        course = utils.CourseFactory(category=self.category, name="Django course")

        self.assertEqual(str(course), "Django course")
        self.assertTrue(course.category, self.category)
        self.assertTrue(course.uuid)

    def test_create_course_with_contacts(self):
        """
            Test that created course object have all related contact models
        """
        course = utils.CourseFactory(category=self.category)

        contact1 = utils.ContactFactory(course=course)
        contact2 = utils.ContactFactory(course=course)

        self.assertEqual(course.contacts.all()[0], contact1)
        self.assertEqual(course.contacts.all()[1], contact2)

    def test_create_course_with_branches(self):
        """
            Test that created course object have all related branch models
        """
        course = utils.CourseFactory(category=self.category)

        branch1 = utils.BranchFactory(course=course)
        branch2 = utils.BranchFactory(course=course)

        self.assertEqual(course.branches.all()[0], branch1)
        self.assertEqual(course.branches.all()[1], branch2)

    def test_create_course_without_category(self):
        """
            Test that course object can't be created without category object
        """
        category = None

        with self.assertRaises(IntegrityError):
            utils.CourseFactory(category=category)

    def test_get_absolute_url(self):
        """
            Test get_absolute_url() method of course model
        """
        course = utils.CourseFactory()
        client = APIClient()
        response = client.get(course.get_absolute_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
