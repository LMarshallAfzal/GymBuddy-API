from rest_framework import serializers
from api.models import Exercise
from .helpers import validation_helpers


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"

    def validate_name(self, value):
        validation_helpers._validate_required_and_max_length(value, "Name", 100)
        return value
    
    def validate_image_urls(self, value):
        """Validates all image URLs."""
        image_fields = ["image1", "image2", "image3", "image4"]
        for field_name in image_fields:
            validation_helpers._validate_image_url(value.get(field_name), field_name)
        return value
    
    def validate(self, data):
        super().validate(data)

        validation_helpers._validate_choices(data, "muscle_group", valid_values=[
            "Chest", "Forearms", "Lats", "Middle Back", "Lower Back", "Neck", "Quadriceps", "Hamstrings", "Calves", "Triceps", "Traps", "Shoulders", "Abdominals", "Glutes", "Biceps", "Adductors", "Abductors"
        ])
        validation_helpers._validate_choices(data, "type", valid_values=[
            "Cardio", "Olympic Weightlifting", "Plyometrics", "Powerlifting", "Strength", "Stretching", "Strongman"
        ])
        validation_helpers._validate_choices(data, "equipment", valid_values=[
            "Bands", "Foam Roll", "Barbell", "Kettlebells", "Body Only", "Machine", "Cable", "Medicine Ball", "Dumbbell", "None", "E-Z Curl Bar", "Other", "Exercise Ball"
        ])

        validation_helpers._validate_at_least_one_image_url(data)

        if not any(value for value in data.values() if value and value.startswith("http")):
            raise serializers.ValidationError("At least one image URL is required.")

        return data
    
    