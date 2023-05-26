import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import config.base as CONFIG

# Configuración del servidor SMTP y las credenciales de autenticación
smtp_host = CONFIG.SMTP_HOST
smtp_port = CONFIG.SMTP_PORT
smtp_username = CONFIG.SMTP_USER
smtp_password = CONFIG.SMTP_PASSWORD

def sendEmail(destination: str, subject: str, body: str):
    
    # Crear el mensaje de correo electrónico
    message = MIMEMultipart()
    message['From'] = CONFIG.SMTP_USER
    message['To'] = destination
    message['Subject'] = subject

    # Cuerpo del correo electrónico
    body = body
    message.attach(MIMEText(body, 'plain'))
    
    response = 'Error to Send Email'

    # Enviar el correo electrónico
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)
        response = 'Success full send Email'
    
    return response
        