import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key = os.getenv("API_KEY")
)

response = client.chat.completions.create(
  model="gpt-4.1-mini-2025-04-14", 
  messages=[{"role": "user", "content": "왜 강남은 강남이라고 할까요?"}],
  temperature=0.0
)

print(response.choices[0].message.content)
print(response)