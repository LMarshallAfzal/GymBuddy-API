from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api.utils import get_secret
from botocore.exceptions import NoCredentialsError
from decouple import config

class ApiKeyAuthentication(BaseAuthentication):
    """
    Custom authentication class for API key authentication.

    This authentication class checks for the presence of a valid API key in the
    'Authorization' header of the request. If the API key is valid, the request
    is considered authenticated; otherwise, an AuthenticationFailed exception is raised.
    """
    def authenticate(self, request):
        """
        Authenticate the request using the provided API key.

        Parameters:
        - request (HttpRequest): The incoming HTTP request.

        Returns:
        - tuple (None, None) if the API key is valid.
        - None if no API key is provided or if the key is invalid.
        
        Raises:
        - AuthenticationFailed: If the provided API key is invalid.
        """
        api_key = request.headers.get("Authorization")

        if request.method == "GET":
            return (None, None)
        
        elif api_key is None:
            raise AuthenticationFailed("No valid API key present")
        
        # elif api_key == config('API_KEY'):
        #     return (None, None)
        # else:
        #     raise AuthenticationFailed("Invalid API Key")
        
        try: 
            secret_name = "prod/gymbuddy/api-key"
            key_pair_name = "API_Key"

            secret_value = get_secret(secret_name, key_pair_name)

            if secret_value is not None and api_key == secret_value:
                return (None, None)
            else:
                raise AuthenticationFailed("Invalid API Key")
            
        except NoCredentialsError:   
            raise AuthenticationFailed("Unable to authenticate due to missing AWS credentials")
        
        except Exception as e:
            print(f"Error retrieving secret from AWS Secrets Manager: {e}")
            fallback_api_key = config('API_Key')
            
            if api_key == fallback_api_key:
                return (None, None)
            else:
                raise AuthenticationFailed("Invalid API Key")