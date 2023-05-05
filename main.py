import requests
import base64
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import json

def encode_text32(text):
  message_bytes = text.encode('utf-8')
  base32_bytes = base64.b32encode(message_bytes)
  return base32_bytes.decode('utf-8')

def send_gmail_base32(password, recipient, subject, content):
  response = {}
  recipient = encode_text32(recipient)
  subject = encode_text32(subject)
  content = encode_text32(content)
  url = f"https://Hex-Gmail.hexhands.repl.co/gmail/base32/{password}/{recipient}/{subject}/{content}"
  response = requests.get(url)
  if response.status_code == 200:
    response = response.text
  else:
    response["return"] = "Error"
  return json.loads(response)

send_gmail_base32("uisqnx8732h8767523nladhf87326784y", "hexhandsman@gmail.com", "Online!", "test")

"""
Ex:
import hexgmail
hexgmail.send_gmail_raw(raw_password, gmail of who to send to, subject, content)

hexgmail.send_gmail_base64(base64_password, gmail of who to send to, subject, content)

hexgmail.send_gmail_base32(base32_password, gmail of who to send to, subject, content)

send_gmail_self(your gmail, your gmail special password (gotten through google), gmail of who to send to, subject, content)

hexgmail.send_gmail_self_attachment(your gmail, your gmail special password (gotten through google), gmail of who to send to, subject, content, [full path file attachment 1, full path file attachment 2, send as many files as you want])

Each command returns a Sent or Error.
Sent = Message sent "not guaranteed arrival"
Error = Message not sent and an error occured

Ex: {"return": "Sent"} or {"return": "Error"}
"""
