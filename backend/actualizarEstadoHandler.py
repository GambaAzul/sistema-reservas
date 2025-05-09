import json
import boto3

dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('Reservas')

def lambda_handler(event, context):
    try:
        datos = json.loads(event['body'])
        reserva_id = datos['reservaId']
        nuevo_estado = datos['estado']

        tabla.update_item(
            Key={'reservaId': reserva_id},
            UpdateExpression='SET estado = :estado',
            ExpressionAttributeValues={':estado': nuevo_estado}
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'mensaje': 'Estado actualizado'})
        }

    except Exception as error:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(error)})
        }
