from django.test import TestCase

from .utils import fake, CategoryFactory
from courses import serializers


class TestCourseSerializers(TestCase):
    """
        Class for testing course serializer
    """

    def test_custom_create(self):
        """
            Testing course serializers create() method can accept list of branches and contacts
        """
        CategoryFactory()

        course_dict = {
            "name": "DJango Course",
            "description": fake.paragraph(nb_sentences=5, variable_nb_sentences=True, ext_word_list=None),
            "logo": fake.file_path(),
            "category": 1,
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
        serializer = serializers.CourseSerializer(data=course_dict)
        self.assertTrue(serializer.is_valid())
