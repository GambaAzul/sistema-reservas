provider "aws" {
  region = "us-east-1"
}

resource "aws_dynamodb_table" "reservas" {
  name           = var.dynamodb_table_name
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "reservaId"

  attribute {
    name = "reservaId"
    type = "S"
  }
}

resource "aws_sns_topic" "confirmacion" {
  name = var.sns_topic_name
}
