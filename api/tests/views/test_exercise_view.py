from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Exercise
from api.views import ExerciseViewSet

class ExerciseViewSetTestCase(APITestCase):
    fixtures = [
        "api/tests/fixtures/exercises.json"
    ]

    def setUp(self):
        self.url = '/exercises/'

    def test_get_all_exercises_url(self):
        self.assertEqual(self.url, f'/exercises/')

    def test_get_exercise_view_is_200_OK(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        exercise_data = response.data["results"]
        self.assertEqual(len(exercise_data), 3)
        names = [exercise['name'] for exercise in exercise_data]
        self.assertIn("Push-up", names)
        self.assertIn("Squat", names)
        self.assertIn("Bicep curl", names)