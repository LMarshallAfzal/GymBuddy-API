from rest_framework import serializers
from api.models import Exercise
import urllib.parse

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"

    def validate_name(self, value):
        if not value or len(value) > 255:
            raise serializers.ValidationError("Name is required and cannot exceed 100 characters.")
        return value
    
    def validate_image1(self, value):
        return self._validate_image_url(value, "image1")

    def validate_image2(self, value):
        return self._validate_image_url(value, "image2")
    
    def validate_image3(self, value):
        return self._validate_image_url(value, "image3")

    def validate_image4(self, value):
        return self._validate_image_url(value, "image4")
    
    def validate(self, data):
        super().validate(data)

        valid_muscle_groups = ["Chest", "Forearms", "Lats", "Middle Back", "Lower Back", "Neck", "Quadriceps", "Hamstrings", "Calves", "Triceps", "Traps", "Shoulders", "Abdominals", "Glutes", "Biceps", "Adductors", "Abductors"]
        if data["muscle_group"] not in valid_muscle_groups:
            raise serializers.ValidationError(
                "Invalid muscle group, it must be one of the following: Chest, Forearms, Lats, Middle Back, Lower Back, Neck, Quadriceps, Hamstrings, Calves, Triceps, Traps, Shoulders, Abdominals, Glutes, Biceps, Adductors, or Abductors"
            )
        
        valid_types = ["Cardio", "Olympic Weightlifting", "Plyometrics", "Powerlifting", "Strength", "Stretching", "Strongman"]
        if data["type"] not in valid_types:
            raise serializers.ValidationError(
                "Invalid exercise type: it must be one of the following: Cardio, Olympic Weightlifting, Plyometrics, Powerlifting, Strength, or Strongman"
            )
        
        valid_equipment = ["Bands", "Foam Roll", "Barbell", "Kettlebells", "Body Only", "Machine", "Cable", "Medicine Ball", "Dumbbell", "None", "E-Z Curl Bar", "Other", "Exercise Ball"]
        if data["equipment"] not in valid_equipment:
            raise serializers.ValidationError(
                "Invalid equipment: it must be one of the following: Bands, Foam Roll, Barbell, Kettlebells, Body Only, Machine, Cable, Medicine, Dumbbell, None, E-Z Bar Curl, Other, Exercise Ball"
            )

        if not any(value for value in data.values() if value and value.startswith("http")):
            raise serializers.ValidationError("At least one image URL is required.")

        return data
    
    def _validate_image_url(self, value, field_name):
        if value:
            try:
                parsed_url = urllib.parse.urlparse(value)
                if not parsed_url.scheme or not parsed_url.netloc:
                    raise serializers.ValidationError(f"{field_name} must be a valid URL.")
            except ValueError:
                raise serializers.ValidationError(f"{field_name} is not a valid URL.")
        return value