from rest_framework import serializers
from api.models import Exercise
import urllib.parse

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"

    def validate_name(self, value):
        self._validate_required_and_max_length(value, "Name", 100)
        return value
    
    def validate_image_urls(self, value):
        """Validates all image URLs."""
        image_fields = ["image1", "image2", "image3", "image4"]
        for field_name in image_fields:
            self._validate_image_url(value.get(field_name), field_name)
        return value
    
    def validate(self, data):
        super().validate(data)

        self._validate_choices(data, "muscle_group", valid_values=[
            "Chest", "Forearms", "Lats", "Middle Back", "Lower Back", "Neck", "Quadriceps", "Hamstrings", "Calves", "Triceps", "Traps", "Shoulders", "Abdominals", "Glutes", "Biceps", "Adductors", "Abductors"
        ])
        self._validate_choices(data, "type", valid_values=[
            "Cardio", "Olympic Weightlifting", "Plyometrics", "Powerlifting", "Strength", "Stretching", "Strongman"
        ])
        self._validate_choices(data, "equipment", valid_values=[
            "Bands", "Foam Roll", "Barbell", "Kettlebells", "Body Only", "Machine", "Cable", "Medicine Ball", "Dumbbell", "None", "E-Z Curl Bar", "Other", "Exercise Ball"
        ])

        self._validate_at_least_one_image_url(data)

        if not any(value for value in data.values() if value and value.startswith("http")):
            raise serializers.ValidationError("At least one image URL is required.")

        return data
    
    def _validate_required_and_max_length(self, value, field_name, max_length):
        if not value or len(value) > max_length:
            raise serializers.ValidationError(f"{field_name} is required and cannot exceed {max_length} characters.")

    def _validate_image_url(self, value, field_name):
        if value:
            try:
                urllib.parse.urlparse(value)
            except ValueError:
                raise serializers.ValidationError(f"{field_name} is not a valid URL.")

    def _validate_choices(self, data, field_name, valid_values):
        if data[field_name] not in valid_values:
            raise serializers.ValidationError(
                f"Invalid {field_name}, it must be one of the following: {', '.join(valid_values)}"
            )

    def _validate_at_least_one_image_url(self, data):
        if not any(value for value in data.values() if value.startswith("http")):
            raise serializers.ValidationError("At least one image URL is required.")