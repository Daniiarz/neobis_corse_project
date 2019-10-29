from rest_framework import serializers
from core.models import Category, Contact, Course, Branch


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category objects, used as a link to Category serializer"""

    class Meta:
        model = Category
        fields = (
            "name",
            "imgpath",
        )


class BranchSerializer(serializers.ModelSerializer):
    """Serializer for Branch objects, used as a link to Category serializer"""

    class Meta:
        model = Category
        fields = (
            "latitude",
            "longitude",
            "value",
        )


class ContactSerializer(serializers.ModelSerializer):
    """Serializer for Contact objects, used as a link to Category serializer"""

    class Meta:
        model = Contact
        fields = (
            "contact_type",
            "value",
        )


class CourseSerializer(serializers.ModelSerializer):
    """Serializer for Course objects, main serializer in this project required to serialize multiple relations"""
    contacts = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all()
    )
    branches = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all()
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = Course
        fields = (
            "name",
            "description",
            "category",
            "uuid",
            "logo",
            "contacts",
            "branches",
        )
