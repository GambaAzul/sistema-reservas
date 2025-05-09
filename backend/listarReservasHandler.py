import json
import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('Reservas')

def lambda_handler(event, context):
    try:
        usuario = event['queryStringParameters']['usuario']
        response = tabla.scan(
            FilterExpression=Attr('usuario').eq(usuario)
        )
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }

    except Exception as error:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(error)})
        }
