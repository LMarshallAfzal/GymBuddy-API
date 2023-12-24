from django.core.exceptions import ValidationError
from django.test import TestCase
# from rest_framework.test import APIClient
from api.models import Exercise

class ExerciseModelTestCase(TestCase):

    def setUp(self):
        self.exercise = Exercise.objects.create (
            name = 'Push-ups',
            description = 'A classic bodyweight exercise for building upper body strength.',
            type = 'Strength',
            muscle_group = 'Chest',
            equipment = 'None',
            level = 'Beginner'
        ) 

    def test_valid_exercise(self):
        self._assert_exercise_is_valid()

    """Tests for exercise name field"""
    def test_exercise_name_must_not_be_blank(self):
        self.exercise.name = ""
        self._assert_exercise_is_invalid()

    def test_exercise_must_not_be_null(self):
        self.exercise.name = None
        self._assert_exercise_is_invalid()

    def test_exercise_name_can_be_255_characters(self):
        self.exercise.name = "x" * 255
        self._assert_exercise_is_valid()

    def test_exercise_name_cannot_be_256_characters(self):
        self.exercise.name = "x" * 256
        self._assert_exercise_is_invalid()

    
    

    def _assert_exercise_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.exercise.full_clean()

    def _assert_exercise_is_valid(self):
        try:
            self.exercise.full_clean()
        except(ValidationError):
            self.fail("Test club should be valid")