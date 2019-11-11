from django.db import models
from django.urls import reverse
import uuid as uuid_lib


class Category(models.Model):
    """Model for Category objects"""
    name = models.CharField(max_length=255)
    imgpath = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    """Model for Course objects"""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4(),
        editable=False
    )
    logo = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("course-detail", kwargs={"pk": self.pk})


class Branch(models.Model):
    """Model for Branch objects"""
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="branches")

    def __str__(self):
        return self.address


class Contact(models.Model):
    """Model for Contact"""
    PHONE = 1
    FACEBOOK = 2
    EMAIL = 3
    CONTACT_CHOICES = (
        (PHONE, "Phone"),
        (FACEBOOK, "Facebook"),
        (EMAIL, "Email")
    )
    contact_type = models.IntegerField(choices=CONTACT_CHOICES)
    value = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="contacts")

    def __str__(self):
        return self.value
