import logging
import base64
import boto3
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

response  = {
    'statusCode': 200,
    'headers': {
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,PUT'
    },
    'body': ''
}

def lambda_handler(event, context):

    file_name = event['headers']['file-name']
    file_content = base64.b64decode(event['body'])
    custom_labels = event['headers']['x-amz-meta-customlabels']
    content_type = event['headers']['content-type']
    
    BUCKET_NAME = 'comse6998-a2-b2'

    try:
        s3_response = s3_client.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=file_content, ContentType=content_type, Metadata={'customlabels': custom_labels})   
        logger.info('S3 Response: {}'.format(s3_response))
        response['body'] = 'Your file has been uploaded'

        return response

    except Exception as e:
        raise IOError(e)    
