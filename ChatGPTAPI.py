import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 0.8,
  max_tokens = 500,
  messages = [
    {"role": "system", "content": "You are a doctor who diagnosis issue with the client"},
    {"role": "user", "content": "I have a headache on the front of my head"},
  ]
)

print(completion.choices[0].message)

