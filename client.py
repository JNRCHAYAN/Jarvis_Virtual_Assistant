
## This feature is paid user only
from openai import OpenAI

client = OpenAI(
    api_key= "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",

)
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a Virtual assistant named roy, skilled in General Task"},
    {"role": "user", "content": "What is what is coding"}
  ]
)

print(completion.choices[0].message.content)


