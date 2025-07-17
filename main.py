from message_sender import send_message
from message_generator import generate_message
import random

feel_good_topics = [
  'cute animal videos',
  'acts of kindness',
  'personal achievements',
  'beautiful nature scenes',
  'nostalgic memories',
  'humor and laughter',
  'gratitude and appreciation',
  'creative accomplishments',
  'human connections',
  'comfort activities'
]

# Select a random feel-good topic
topic = random.choice(feel_good_topics)

prompt = f"Please create one sentence about {topic}. Do not provide multiple options to choose from. Please print only the message."

response = generate_message(prompt)
send_message(response)
