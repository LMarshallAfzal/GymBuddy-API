from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True  
        elif request.auth and request.auth.type == 'api-key':
            return True  
        return False
    
