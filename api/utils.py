import boto3
import json
from botocore.exceptions import ClientError

def get_secret(secret_name, key_pair_name):
    """
    Retrieve the a key value from AWS Secrets Manager.

    Parameters:
    - secret_name (str): The name or ARN of the secret containing the secret key/value pair.

    Returns:
    - str: The key value.

    Raises:
    - AuthenticationFailed: If an error occurs while retrieving the secret.
    """
    client = boto3.client(
        service_name='secretsmanager',
        region_name='eu-west-2'
    )

    try:
        response =  client.get_secret_value(SecretId=secret_name)
        secret = response['SecretString']
        secret_dict = json.loads(secret)
        secret_value = secret_dict.get(key_pair_name)

        return secret_value
    
    except ClientError as e:
        print(f"Error retrieving secret from AWS Secrets Manager: {e}")
        return None