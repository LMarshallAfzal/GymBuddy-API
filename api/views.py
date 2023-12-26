from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from api.serializers import ExerciseSerializer
from api.models import Exercise

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.get_all_exercises()
    serializer_class = ExerciseSerializer
    
