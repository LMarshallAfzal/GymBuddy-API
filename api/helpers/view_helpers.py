from rest_framework import serializers

def _get_queryset(self, name=None):
        """Helper function to retrieve and filter exercises."""
        queryset = self.queryset.filter(name=name) if name else self.queryset.all()
        return queryset