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

    """Tests for exercise description field"""
    def test_exercise_description_can_be_blank(self):
        self.exercise.description = ""
        self._assert_exercise_is_valid()

    def test_exercise_description_can_be_null(self):
        self.exercise.description = None
        self._assert_exercise_is_valid()

    """Tests for exercise type field"""
    def test_exercise_type_can_be_blank(self):
        self.exercise.type = ""
        self._assert_exercise_is_valid()

    def test_exercise_type_must_can_be_null(self):
        self.exercise.type = None
        self._assert_exercise_is_valid()
    
    def test_exercise_type_can_be_25_characters(self):
        self.exercise.type = "x" * 25
        self._assert_exercise_is_valid()

    def test_exercise_type_cannot_be_26_characters(self):
        self.exercise.type = "x" * 26
        self._assert_exercise_is_invalid()
    
    """Tests for exercise muscle group field"""
    def test_exercise_muscle_group_can_be_blank(self):
        self.exercise.muscle_group = ""
        self._assert_exercise_is_valid()

    def test_exercise_muscle_group_can_be_null(self):
        self.exercise.muscle_group = None
        self._assert_exercise_is_valid()
    
    def test_exercise_muscle_group_can_be_30_characters(self):
        self.exercise.muscle_group = "x" * 30
        self._assert_exercise_is_valid()

    def test_exercise_muscle_group_cannot_be_31_characters(self):
        self.exercise.muscle_group = "x" * 31
        self._assert_exercise_is_invalid()
    
    """Tests for exercise equipment field"""
    def test_exercise_equipment_can_be_blank(self):
        self.exercise.equipment = ""
        self._assert_exercise_is_valid()

    def test_exercise_equipment_can_be_null(self):
        self.exercise.equipment = None
        self._assert_exercise_is_valid()
    
    def test_exercise_equipment_can_be_15_characters(self):
        self.exercise.equipment = "x" * 15
        self._assert_exercise_is_valid()

    def test_exercise_equipment_cannot_be_16_characters(self):
        self.exercise.equipment = "x" * 16
        self._assert_exercise_is_invalid()
    
    """Tests for exercise level field"""
    def test_exercise_level_can_be_blank(self):
        self.exercise.level = ""
        self._assert_exercise_is_valid()

    def test_exercise_level_can_be_null(self):
        self.exercise.level = None
        self._assert_exercise_is_valid()
    
    def test_exercise_level_can_be_15_characters(self):
        self.exercise.level = "x" * 15
        self._assert_exercise_is_valid()

    def test_exercise_level_cannot_be_16_characters(self):
        self.exercise.level = "x" * 16
        self._assert_exercise_is_invalid()

    def _assert_exercise_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.exercise.full_clean()

    def _assert_exercise_is_valid(self):
        try:
            self.exercise.full_clean()
        except(ValidationError):
            self.fail("Test club should be valid")