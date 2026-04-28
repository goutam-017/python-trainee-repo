from groq import Groq
import os
prompt=input("Enter your prompt: ")
client=Groq(api_key=os.getenv("API_KEY"))
response=client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role":"user","content":prompt}],
)
print(response.choices[0].message.content)