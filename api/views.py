from rest_framework import viewsets
from api.serializers import ExerciseSerializer
from api.models import Exercise

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.get_all_exercises()
    serializer_class = ExerciseSerializer
    
