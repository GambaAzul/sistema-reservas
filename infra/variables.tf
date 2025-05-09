variable "region" {
  description = "Región donde se desplegarán los recursos"
  type        = string
  default     = "us-east-1"
}

variable "sns_topic_name" {
  description = "Nombre del topic SNS para notificaciones"
  type        = string
  default     = "ConfirmacionReservas"
}

variable "dynamodb_table_name" {
  description = "Nombre de la tabla DynamoDB"
  type        = string
  default     = "Reservas"
}
