import json
import requests
import boto3
import base64
from botocore.exceptions import ClientError
from getsecrets import get_secret


def lambda_handler(event, context):
    # TODO implement

    # Set the request parameters
    url = 'https://dev58618.service-now.com/api/now/import/u_ec2_tracker'

    # Eg. User name="admin", Password="admin" for this code sample.
    user = 'admin'
    pwd = 'password'
    payload = "{\"u_instance_id\":\"\",\"u_instance_state\":\"\",\"u_private_ip\":\"\",\"u_public_ip\":\"\",\"sys_updated_on\":\"\"}"

    # Set proper headers
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}

    # Do the HTTP request
    response = requests.post(url, auth=(user, pwd),
                             headers=headers, data=payload)

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:',
              response.headers, 'Error Response:', response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully uploaded to Servicenow.')

    }
