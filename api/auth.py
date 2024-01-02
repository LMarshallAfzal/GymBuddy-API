from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from decouple import config

class ApiKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get("Authorization")

        if not api_key:
            return None
        
        if api_key == config('API_KEY'):
            return (None, None)
        else:
            raise AuthenticationFailed("Invalid API Key")