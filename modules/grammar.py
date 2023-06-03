from chipline_openai import prompt, create

response = create(
  model="text-davinci-003",
  prompt=f"Correct this to standard English:\n\n{prompt}",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
