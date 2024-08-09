
## This feature is paid user only
from openai import OpenAI

client = OpenAI(
    api_key= "#",

)
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a Virtual assistant named roy, skilled in General Task"},
    {"role": "user", "content": "What is what is coding"}
  ]
)

print(completion.choices[0].message.content)


