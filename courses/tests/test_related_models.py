from django.test import TestCase
from django.db.utils import IntegrityError

from . import utils


class TestRelatedModels(TestCase):
    """
        Class for testing models that related to course model
    """
    def setUp(self) -> None:
        self.course = utils.CourseFactory()

    def test_create_branch_model(self):
        """
            Test creation of branch model and work of its __str__ method
        """
        address = utils.fake.address()
        branch = utils.BranchFactory(course=self.course, address=address)

        self.assertTrue(str(branch), address)

    def test_branch_without_course(self):
        """
            Test that branch model can't be created without course object
        """
        course = None
        with self.assertRaises(IntegrityError):
            branch = utils.BranchFactory(course=course)

    def test_create_contact_model(self):
        """
            Test creation of contact model and work of its __str__ method
        """
        value = utils.fake.phone_number()
        contact = utils.ContactFactory(course=self.course, value=value)

        self.assertTrue(str(contact), value)

    def test_contact_without_course(self):
        """
            Test that contact model can't be created without course object
        """
        course = None
        with self.assertRaises(IntegrityError):
            contact = utils.ContactFactory(course=course)

    def test_create_category_model(self):
        """
            Test creation of category model and work of its __str__ method
        """
        name = "Django"
        contact = utils.CategoryFactory(name=name)

        self.assertTrue(str(contact), name)
