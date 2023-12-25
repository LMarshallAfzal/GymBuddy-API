from rest_framework import viewsets
from api.serializers import ExerciseSerializer, ImageSerializer
from api.models import Exercise, Image

class ExerciseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Exercise.get_all_exercises()
    serializer_class = ExerciseSerializer

class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Image.get_all_images()
    serializer_class = ImageSerializer
