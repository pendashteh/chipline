import openai
import sys

prompt = sys.argv[1]

openai.api_key_path = 'openai_api_key'

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

print(response)
