from django.core.exceptions import ValidationError
from django.test import TestCase
from api.models import Image, Exercise

class ImageModelTestCase(TestCase):
    def setUp(self):
        self.exercise = Exercise.objects.create(name="Test Exercise")

    def test_valid_image(self):
        image = Image.objects.create(
            url = "https://example.com/image.jpg",
            exercise=self.exercise
        )
        self._assert_image_is_valid(image)

    """Tests for image url field"""
    def test_image_url_is_required(self):
        image = Image(exercise=self.exercise)
        self._assert_image_is_invalid(image)

    def test_image_url_has_max_length(self):
        image = Image(url="x" * 501, exercise=self.exercise)
        self._assert_image_is_invalid(image)

    def test_image_url_can_be_500_characters(self):
        image = Image(url='x' * 500, exercise=self.exercise)
        self._assert_image_is_valid(image)

    """Tests for exercise foreign key field"""
    def test_exercise_is_required(self):
        image = Image(url='https://example.com/image.jpg')
        self._assert_image_is_invalid(image)

    def test_image_can_be_deleted_with_exercise(self):
        image = Image.objects.create(
            url="https://example.com/image.jpg",
            exercise=self.exercise
        )
        self.exercise.delete()
        self.assertFalse(Image.objects.exists())

    def _assert_image_is_invalid(self, image):
        with self.assertRaises(ValidationError):
            image.full_clean()

    def _assert_image_is_valid(self, image):
        try:
            image.full_clean()
        except ValidationError:
            self.fail("Image should be valid")
