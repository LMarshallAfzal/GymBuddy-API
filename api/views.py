from rest_framework import viewsets, status
from rest_framework.response import Response

from api.auth import ApiKeyAuthentication
from api.serializers import ExerciseSerializer
from api.helpers import view_helpers
from api.models import Exercise

class ExerciseViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing exercise data.

    Provides actions for retrieving, creating, updating, and deleting exercises.
    """
    queryset = Exercise.get_all_exercises()
    serializer_class = ExerciseSerializer
    authentication_classes=[ApiKeyAuthentication]

    def list(self, request):
        """
        Retrieve a list of exercises.

        Optionally filter exercises by name.

        Parameters
        ----------
        name (str, optional): Filter exercises by name.

        Returns
        -------
        Response
            A JSON response containing a list of exercise data.
        """
        name = request.query_params.get('name')
        queryset = self.view_helpers._get_queryset(name=name)
        serializer = self.get_serializer(queryset, many=True)

        if not serializer.data:
            return Response({"error": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.data)
    
    def create(self, request):
        """
        Create a new exercise.

        Deserializes the request data and creates a new exercise instance.

        Parameters
        ----------
        request.data (dict): The request data containing exercise information.

        Returns
        -------
        Response
            A JSON response containing the newly created exercise data and a 201 Created status code.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, pk=None):
        """
        Update an existing exercise.

        Retrieves the exercise instance with the specified ID, deserializes the request data,
        and updates the exercise with the new information.

        Parameters
        ----------
        pk (int): The primary key of the exercise to update.
        request.data (dict): The request data containing updated exercise information.

        Returns
        -------
        Response
            A JSON response containing the updated exercise data.
        """
        exercise = self.get_object()
        serializer = self.get_serializer(exercise, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    