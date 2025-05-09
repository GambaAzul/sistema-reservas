import json
import boto3

dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('Reservas')

def lambda_handler(event, context):
    try:
        reserva_id = event['pathParameters']['reservaId']
        tabla.update_item(
            Key={'reservaId': reserva_id},
            UpdateExpression='SET estado = :estado',
            ExpressionAttributeValues={':estado': 'cancelado'}
        )
        return {
            'statusCode': 200,
            'body': json.dumps({'mensaje': 'Reserva cancelada'})
        }

    except Exception as error:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(error)})
        }
