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
        model = Branch
        fields = (
            "latitude",
            "longitude",
            "address",
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
    contacts = ContactSerializer(
        many=True,
    )
    branches = BranchSerializer(
        many=True,
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

        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        branches_data = validated_data.pop("branches")
        contacts_data = validated_data.pop("contacts")
        course = Course.objects.create(**validated_data)

        for branch_data in branches_data:
            Branch.objects.create(course=course, **branch_data)

        for contact_data in contacts_data:
            Contact.objects.create(course=course, **contact_data)

        return course
