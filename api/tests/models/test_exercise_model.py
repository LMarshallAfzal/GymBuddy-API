from django.core.exceptions import ValidationError
from django.test import TestCase
from api.models import Exercise

class ExerciseModelTestCase(TestCase):

    def setUp(self):
        self.exercise = Exercise.objects.create (
            name = 'Push-ups',
            description = 'A classic bodyweight exercise for building upper body strength.',
            type = 'Strength',
            muscle_group = 'Chest',
            equipment = 'None',
            level = 'Beginner',
            image1 = "https://example.com/image.jpg",
            image2 = "https://example.com/image.jpg",
            image3 = "https://example.com/image.jpg",
            image4 = "https://example.com/image.jpg",
        )
        self.exercise_2 = Exercise.objects.create(
            name="Squat", 
            type="Strength", 
            muscle_group="Legs"
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

    """Tests for image 1 field"""
    def test_exercise_image_1_can_be_blank(self):
        self.exercise.image1 = ""
        self._assert_exercise_is_valid()

    def test_exercise_image_1_can_be_null(self):
        self.exercise.image1 = None
        self._assert_exercise_is_valid()
    
    def test_exercise_image_1_can_be_500_characters(self):
        self.exercise.image1 = "x" * 500
        self._assert_exercise_is_valid()

    def test_exercise_image_1_cannot_be_501_characters(self):
        self.exercise.image1 = "x" * 501
        self._assert_exercise_is_invalid()

    """Tests for image 2 field"""
    def test_exercise_image_2_can_be_blank(self):
        self.exercise.image2 = ""
        self._assert_exercise_is_valid()

    def test_exercise_image_2_can_be_null(self):
        self.exercise.image2 = None
        self._assert_exercise_is_valid()
    
    def test_exercise_image_2_can_be_500_characters(self):
        self.exercise.image2 = "x" * 500
        self._assert_exercise_is_valid()

    def test_exercise_image_2_cannot_be_501_characters(self):
        self.exercise.image2 = "x" * 501
        self._assert_exercise_is_invalid()

    """Tests for image 3 field"""
    def test_exercise_image_3_can_be_blank(self):
        self.exercise.image3 = ""
        self._assert_exercise_is_valid()

    def test_exercise_image_3_can_be_null(self):
        self.exercise.image3 = None
        self._assert_exercise_is_valid()
    
    def test_exercise_image_3_can_be_500_characters(self):
        self.exercise.image3 = "x" * 500
        self._assert_exercise_is_valid()

    def test_exercise_image_3_cannot_be_501_characters(self):
        self.exercise.image3 = "x" * 501
        self._assert_exercise_is_invalid()

    """Tests for image 4 field"""
    def test_exercise_image_4_can_be_blank(self):
        self.exercise.image4 = ""
        self._assert_exercise_is_valid()

    def test_exercise_image_4_can_be_null(self):
        self.exercise.image4 = None
        self._assert_exercise_is_valid()
    
    def test_exercise_image_4_can_be_500_characters(self):
        self.exercise.image4 = "x" * 500
        self._assert_exercise_is_valid()

    def test_exercise_image_4_cannot_be_501_characters(self):
        self.exercise.image4 = "x" * 501
        self._assert_exercise_is_invalid()

    def test_get_all_exercises(self):
        exercises = Exercise.get_all_exercises()
        self.assertEqual(exercises.count(), 2)

    def _assert_exercise_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.exercise.full_clean()

    def _assert_exercise_is_valid(self):
        try:
            self.exercise.full_clean()
        except(ValidationError):
            self.fail("Test club should be valid")