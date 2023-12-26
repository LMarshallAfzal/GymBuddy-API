from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from api.serializers import ExerciseSerializer
from api.models import Exercise

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.get_all_exercises()
    serializer_class = ExerciseSerializer

    def list(self, request):
        name = request.query_params.get('name')
        if name:
            queryset = self.queryset.filter(name=name)
        else:
            queryset = self.queryset.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    
    