import chipline_openai

response = chipline_openai.create(
  model="text-davinci-003",
  prompt=f"""
  The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
  Human: {chipline_openai.prompt}
  AI:
  """,
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)
