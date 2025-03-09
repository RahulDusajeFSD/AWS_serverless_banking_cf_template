


import json
import boto3

client = boto3.client('s3')

def lambda_handler(event, context):
    response = client.get_object(
        Bucket= '',
        Key=''
    )
    
    data_byte= response['Body'].read()
    
    data_String = data_byte.decode('UTF-8')
    
    data_dict=json.loads(data_String)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(data_dict),
        'headers': {
            'Content-Type': 'application/json'
        }
    }