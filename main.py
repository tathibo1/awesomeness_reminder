from message_sender import send_message
from message_generator import generate_message

prompt = "Please create one sentence to make someone feel good. Do not provide multiple options to choose from. Please print only the message."
response = generate_message(prompt)
send_message(response)
