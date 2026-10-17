from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            "id",
            "first_name",
            "last_name",
            "age",
            "uploaded_file",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_age(self, value):
        if value > 120:
            raise serializers.ValidationError(
                "Age must not exceed 120."
            )
        return value

    def validate_uploaded_file(self, value):
        if value and value.size > 10 * 1024 * 1024:
            raise serializers.ValidationError(
                "File size must not exceed 10 MB."
            )
        return value