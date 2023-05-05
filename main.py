import requests
import base64
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import json
import os

print("Started!")

def encode_text32(text):
  message_bytes = text.encode('utf-8')
  base32_bytes = base64.b32encode(message_bytes)
  return base32_bytes.decode('utf-8')

def send_gmail_base32(password, recipient, subject, content):
  recipient = encode_text32(recipient)
  subject = encode_text32(subject)
  content = encode_text32(content)
  url = f"https://Hex-Gmail.hexhands.repl.co/gmail/base32/{password}/{recipient}/{subject}/{content}"
  response = requests.get(url)
  if response.status_code == 200:
    try:
      return response.json()
    except json.JSONDecodeError:
      print("ERROR: Response not valid JSON. Response text:")
      print(response.text)
      return None
  else:
    print(f"ERROR: Non-200 response. Status code: {response.status_code}")
    return None

result = send_gmail_base32(os.environ['PASSWORD'], "hexhandsman@gmail.com", "Online!", "test")
print(result)
