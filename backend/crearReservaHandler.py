import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
tabla = dynamodb.Table('Reservas')
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:541308266237:ConfirmacionReservas"

def lambda_handler(event, context):
    try:
        datos = json.loads(event['body'])
        reserva_id = str(uuid.uuid4())
        fecha = datetime.utcnow().isoformat()

        item = {
            'reservaId': reserva_id,
            'usuario': datos['usuario'],
            'fecha_reserva': datos['fecha_reserva'],
            'hora': datos['hora'],
            'cancha': datos['cancha'],
            'estado': 'pendiente',
            'timestamp': fecha
        }

        tabla.put_item(Item=item)

        mensaje = f"""Nueva reserva creada:
Usuario: {datos['usuario']}
Fecha: {datos['fecha_reserva']}
Hora: {datos['hora']}
Cancha: {datos['cancha']}"""

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=mensaje.strip(),
            Subject='Reserva confirmada'
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'mensaje': 'Reserva registrada exitosamente',
                'id': reserva_id
            })
        }

    except Exception as error:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(error)})
        }
