import json
from datetime import datetime

def lambda_handler(event, context):
    try:
        datos = json.loads(event['body'])
        fecha_reserva = datos['fecha_reserva']

        if fecha_reserva < datetime.utcnow().strftime('%Y-%m-%d'):
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No se permiten fechas pasadas'})
            }

        return {
            'statusCode': 200,
            'body': json.dumps({'mensaje': 'Validación correcta'})
        }

    except Exception as error:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(error)})
        }
