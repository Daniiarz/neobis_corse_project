import factory
from faker import Faker
from core import models
import random

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    """
        Factory for creating random Category models
    """

    class Meta:
        model = models.Category

    name = factory.Sequence(lambda n: f"Category-{n}")
    imgpath = fake.file_path(extension="jpeg")


class CourseFactory(factory.django.DjangoModelFactory):
    """
        Factory for creating random Course models
    """

    class Meta:
        model = models.Course

    name = factory.Sequence(lambda n: f"Course-{n}")
    description = fake.paragraph(nb_sentences=5, variable_nb_sentences=True, ext_word_list=None)
    logo = fake.file_path(extension="jpeg")
    category = factory.SubFactory(CategoryFactory)


class BranchFactory(factory.django.DjangoModelFactory):
    """
        Factory for creating random Branch models
    """

    class Meta:
        model = models.Branch

    latitude = fake.zipcode_plus4()
    longitude = fake.zipcode_plus4()
    address = fake.address()
    course = factory.SubFactory(CourseFactory)


class ContactFactory(factory.django.DjangoModelFactory):
    """
        Factory for creating random Contact models
    """

    class Meta:
        model = models.Contact

    contact_type = random.randint(1, 3)
    value = fake.phone_number()
    course = factory.SubFactory(CourseFactory)
