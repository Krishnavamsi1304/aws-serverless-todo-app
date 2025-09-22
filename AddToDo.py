# add_todo_handler.py
import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    todo_id = str(uuid.uuid4())
    item = {
        'id': todo_id,
        'task': body['task'],
        'completed': False
    }
    table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'ToDo added!', 'id': todo_id})
    }
