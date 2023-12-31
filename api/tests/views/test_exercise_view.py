import pytest
from rest_framework.test import APITestCase
from rest_framework import status
from api.views import ExerciseViewSet
from api.models import Exercise

class ExerciseViewSetTestCase(APITestCase):
    fixtures = [
        "api/tests/fixtures/exercises.json"
    ]

    def setUp(self):
        self.url = '/exercises/'
        self.base_exercise_data = {
            "name": "Hip Lift with Band",
            "description": "Lift your hips up with a band over your waist attached to weights",
            "type": "Powerlifting",
            "muscle_group": "Calves",
            "equipment": "Bands",
            "level": "Beginner",
            "image1": "https://www.bodybuilding.com/exercises/exerciseImages/sequences/738/Female/l/738_1.jpg",
            "image2": "https://www.bodybuilding.com/exercises/exerciseImages/sequences/738/Female/l/738_2.jpg"
        }

        self.post_form_input = {**self.base_exercise_data, "id": 7}
        self.put_form_input = {**self.base_exercise_data, "id": 2}

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

    def test_create_exercise_success(self):
        before = Exercise.objects.count()
        response = self.client.post(self.url, self.post_form_input)
        after = Exercise.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(after, before + 1)

    def test_create_exercise_invalid_name(self):
        invalid_names = [
            "",  
            "X" * 256,
        ]
        for invalid_name in invalid_names:
            self.post_form_input["name"] = invalid_name
            response = self.client.post(self.url, self.post_form_input)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("name", response.data)

    def test_create_exercise_invalid_muscle_group(self):
        invalid_muscle_groups = [
            "",  
            "Invalid Muscle Group",
            "Invalid!@#$%^&*()", 
        ]
        for invalid_muscle_group in invalid_muscle_groups:
            self.post_form_input["muscle_group"] = invalid_muscle_group
            response = self.client.post(self.url, self.post_form_input)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("Invalid muscle_group", response.data["non_field_errors"][0])

    def test_create_exercise_invalid_type(self):
        self.post_form_input["type"] = "Invalid Exercise Type"
        response = self.client.post(self.url, self.post_form_input)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Invalid type", response.data["non_field_errors"][0])

    def test_create_exercise_invalid_image_urls(self):
        invalid_image_urls = [
            ("", "", "", ""),
            ("invalid_url", "", "", ""),
            ("", "invalid_url", "", ""),  
            ("", "", "invalid_url", ""), 
            ("", "", "", "invalid_url"),  
        ]
        for image1, image2, image3, image4 in invalid_image_urls:
            self.post_form_input["image1"] = image1
            self.post_form_input["image2"] = image2
            self.post_form_input["image3"] = image3
            self.post_form_input["image4"] = image4
            response = self.client.post(self.url, self.post_form_input)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertTrue("non_field_errors" in response.data or "image1" in response.data or "image2" in response.data or "image3" in response.data or "image4" in response.data)

            if "non_field_errors" in response.data:
                self.assertEqual(response.data["non_field_errors"][0], "At least one image URL is required.")  # Assert specific error for lack of valid images
            else:
                for key, value in response.data.items():
                    if key in ["image1", "image2", "image3", "image4"]:
                        self.assertEqual(value[0], "Enter a valid URL.")

    def test_create_exercise_invalid_equipment(self):
        invalid_equipment = [
            "",  
            "Invalid Equipment",
            "Invalid Equipment#", 
            "@#$%^&*()",  
        ]
        for invalid_equipment in invalid_equipment:
            self.post_form_input["equipment"] = invalid_equipment
            response = self.client.post(self.url, self.post_form_input)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("equipment", response.data)

    def test_create_exercise_invalid_equipment(self):
        self.post_form_input["equipment"] = "Invalid Equipment"
        response = self.client.post(self.url, self.post_form_input)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("equipment", response.data)

    def test_update_exercise_success_data(self):
        exercise_id = self.put_form_input["id"]
        url = f"{self.url}{exercise_id}/"
        response = self.client.put(url, self.put_form_input)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.pop("id"), self.put_form_input.pop("id"))  

    def test_update_exercise_not_found(self):
        exercise_id = 100
        url = f"{self.url}{exercise_id}/"
        response = self.client.put(url, self.put_form_input)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_exercise_invalid_name(self):
        invalid_names = [
            "",  
            "X" * 256,  
        ]
        for invalid_name in invalid_names:
            input = self.put_form_input.copy() 
            input["name"] = invalid_name
            response = self.client.put(f"{self.url}{self.put_form_input['id']}/", input)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("name", response.data)  

    def test_update_exercise_invalid_muscle_group(self):
        invalid_muscle_groups = [
            "", 
            "Invalid Muscle Group",
            "Invalid!@#$%^&*()", 
        ]
        for invalid_muscle_group in invalid_muscle_groups:
            input = self.put_form_input.copy()
            input["muscle_group"] = invalid_muscle_group
            response = self.client.put(f"{self.url}{self.put_form_input['id']}/", input)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("Invalid muscle_group", response.data["non_field_errors"][0])

    def test_update_exercise_invalid_images(self):
        invalid_image_urls = [
            ("", "", "", ""), 
            ("invalid_url", "", "", ""), 
            ("", "invalid_url", "", ""),  
            ("", "", "invalid_url", ""),  
            ("", "", "", "invalid_url"),  
        ]
        for image1, image2, image3, image4 in invalid_image_urls:
            input = self.put_form_input.copy()
            input["image1"] = image1
            input["image2"] = image2
            input["image3"] = image3
            input["image4"] = image4
            response = self.client.put(f"{self.url}{self.put_form_input['id']}/", input)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertTrue("non_field_errors" in response.data or "image1" in response.data or "image2" in response.data or "image3" in response.data or "image4" in response.data)  

            if "non_field_errors" in response.data:
                self.assertEqual(response.data["non_field_errors"][0], "At least one image URL is required.")  
            else:
                for key, value in response.data.items():
                    if key in ["image1", "image2", "image3", "image4"]:
                        self.assertEqual(value[0], "Enter a valid URL.")

    def test_update_exercise_invalid_equipment(self):
        invalid_equipment = [
            "",  
            "Invalid Equipment",
            "Invalid Equipment#", 
            "@#$%^&*()",  
        ]
        for invalid_equipment in invalid_equipment:
            input = self.put_form_input.copy()
            input["equipment"] = invalid_equipment
            response = self.client.put(f"{self.url}{self.put_form_input['id']}/", input)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertTrue("non_field_errors" in response.data or "equipment" in response.data)

    def test_update_exercise_invalid_data(self):
        exercise_id = self.put_form_input["id"]
        url = f"{self.url}{exercise_id}/"
        input = self.put_form_input
        input["name"] = ""
        response = self.client.put(url, input)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    

