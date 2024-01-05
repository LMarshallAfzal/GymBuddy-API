from rest_framework import serializers
from api.models import Exercise
from api.helpers import validation_helpers


class ExerciseSerializer(serializers.ModelSerializer):
    """
    Serializer for Exercise models, handling validation and serialization of exercise data.
    """
    class Meta:
        model = Exercise
        fields = "__all__"

    def validate_name(self, value):
        """
        Validates the exercise name.

        Args:
            value (str): The provided name value.

        Raises:
            serializers.ValidationError: If the name is empty, exceeds 100 characters, or is invalid.

        Returns:
            str: The validated name value.
        """
        validation_helpers._validate_required_and_max_length(value, "Name", 255)
        return value
    
    def validate_image_urls(self, value):
        """
        Validates all image URLs.

        Args:
            value (dict): The dictionary containing image URL fields.

        Raises:
            serializers.ValidationError: If any of the image URLs are invalid.

        Returns:
            dict: The validated dictionary of image URLs.
        """
        image_fields = ["image1", "image2", "image3", "image4"]
        for field_name in image_fields:
            validation_helpers._validate_image_url(value.get(field_name), field_name)
        return value
    
    def validate(self, data):
        """
        Performs overall validation of exercise data, including:
        - Validating muscle group, exercise type, and equipment against allowed values.
        - Ensuring at least one image URL is provided.

        Args:
            data (dict): The complete exercise data to be validated.

        Raises:
            serializers.ValidationError: If any validation rules are violated.

        Returns:
            dict: The validated exercise data.
        """
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

        return data
    
    