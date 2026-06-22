output "public_ip" {
  value = aws_instance.app_server.public_ip
}

output "swagger_url" {
  value = "http://${aws_instance.app_server.public_ip}:8001/docs"
}
