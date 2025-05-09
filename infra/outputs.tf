output "sns_topic_arn" {
  description = "ARN del SNS Topic"
  value       = aws_sns_topic.confirmacion.arn
}

output "dynamodb_table_name" {
  description = "Nombre de la tabla DynamoDB creada"
  value       = aws_dynamodb_table.reservas.name
}
