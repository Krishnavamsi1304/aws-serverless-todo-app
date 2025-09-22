# update_todo_handler.py
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    todo_id = event['pathParameters']['id']
    response = table.update_item(
        Key={'id': todo_id},
        UpdateExpression='SET task=:task, completed=:completed',
        ExpressionAttributeValues={
            ':task': body['task'],
            ':completed': body['completed']
        },
        ReturnValues='UPDATED_NEW'
    )
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'ToDo updated!', 'attributes': response['Attributes']})
    }
