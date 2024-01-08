from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import boto3
import json
from botocore.exceptions import NoCredentialsError
from decouple import config

class ApiKeyAuthentication(BaseAuthentication):
    """
    Custom authentication class for API key authentication.

    This authentication class checks for the presence of a valid API key in the
    'Authorization' header of the request. If the API key is valid, the request
    is considered authenticated; otherwise, an AuthenticationFailed exception is raised.

    Note: This implementation uses a static API key stored in the project's configuration.
    For production, consider more secure methods such as dynamic key generation or integration
    with a secure vault service.
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
            secret_value = self.get_secret(secret_name)


            if api_key == secret_value:
                return (None, None)
            else:
                print(secret_value)
                raise AuthenticationFailed("Invalid API Key")
            
        except NoCredentialsError:   
            raise AuthenticationFailed("Unable to authenticate due to missing AWS credentials")
        
    def get_secret(self, secret_name):
        client = boto3.client(
            service_name='secretsmanager',
            region_name='eu-west-2'
        )

        try:
            response =  client.get_secret_value(SecretId=secret_name)
            secret_value = response['SecretString']
            secret_dict = json.loads(secret_value)
            api_key_value = secret_dict.get("API_Key")

            return api_key_value
        
        except Exception as e:
            raise AuthenticationFailed(f"Error retrieving secret from AWS Secrets Manager: {e}")