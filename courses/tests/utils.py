import factory
from faker import Faker
from core import models

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
    category = 


class BranchFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Branch


