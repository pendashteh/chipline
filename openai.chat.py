import openai
import sys
import json

prompt = sys.argv[1]

openai.api_key_path = 'key'

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"""
  The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
  Human: {prompt}
  AI:
  """,
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)

text_values = [choice.get('text') for choice in response.get('choices', [])]

print(text_values)

