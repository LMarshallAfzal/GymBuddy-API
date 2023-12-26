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
        queryset = self.queryset.filter(name=name) if name else self.queryset.all()
        serializer = self.get_serializer(queryset, many=True)

        if not serializer.data:
            return Response({"error": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.data)