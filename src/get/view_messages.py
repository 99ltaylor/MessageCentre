import boto3
import json

s3_client = boto3.client('s3')

def handler(event, context):
    # S3 bucket and file details
    bucket_name = 's3-message-storage'
    file_key = 'messages.json'

    try:
        # Download JSON file from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        data = json.loads(response['Body'].read())

        # Extract messages from the JSON data
        messages = data.get('messages', [])

        return {
            'statusCode': 200,
            'body': json.dumps(data),
            'headers': {}
        }

    except Exception as e:
        print(f"Error handling request: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({"error": "Internal Server Error"}),
            'headers': {}
        }
