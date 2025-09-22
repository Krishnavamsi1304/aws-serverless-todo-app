# get_todos_handler.py
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def lambda_handler(event, context):
    response = table.scan()
    todos = response.get('Items', [])
    return {
        'statusCode': 200,
        'body': json.dumps(todos)
    }
