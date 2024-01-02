from rest_framework import serializers
import urllib.parse

def _validate_required_and_max_length(value, field_name, max_length):
        if not value or len(value) > max_length:
            raise serializers.ValidationError(f"{field_name} is required and cannot exceed {max_length} characters.")

def _validate_image_url(value, field_name):
    if value:
        try:
            urllib.parse.urlparse(value)
        except ValueError:
            raise serializers.ValidationError(f"{field_name} is not a valid URL.")

def _validate_choices(data, field_name, valid_values):
    if data[field_name] not in valid_values:
        raise serializers.ValidationError(
            f"Invalid {field_name}, it must be one of the following: {', '.join(valid_values)}"
        )

def _validate_at_least_one_image_url(data):
    if not any(value and value.startswith("http") for value in data.values()):
        raise serializers.ValidationError("At least one image URL is required.")