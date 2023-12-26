from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.views import ExerciseViewSet
import os

class ExerciseViewSetTestCase(APITestCase):
    fixtures = [
        "api/tests/fixtures/exercises.json"
    ]

    def setUp(self):
        self.url = '/exercises/'

    def test_get_all_exercises_url(self):
        self.assertEqual(self.url, f'/exercises/')

    def test_get_all_exercises_success(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        names = [exercise['name'] for exercise in response.data]
        self.assertIn("Push-up", names)
        self.assertIn("Squat", names)
        self.assertIn("Bicep curl", names)

    def test_get_exercise_by_name_success(self):
        exercise_name = "Squat"
        url = f"{self.url}?name={exercise_name}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], exercise_name)

    def test_get_exercise_by_name_not_found(self):
        exercise_name = "Non-existent exercise"
        url = f"{self.url}?name={exercise_name}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_exercise_by_name_missing_name_parameter(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_exercise_by_id_success(self):
        exercise_id = 2
        url = f"{self.url}{exercise_id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 11)

    def test_get_exericse_by_id_not_found(self):
        exercise_id = 10
        url = f"{self.url}{exercise_id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

