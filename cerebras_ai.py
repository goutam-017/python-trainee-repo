import os
from cerebras.cloud.sdk import Cerebras

client=Cerebras(api_key=os.getenv("CEREBRAS_API_KEY"))

response=client.chat.completions.create(
    messages=[{"role":"user","content":"Why we learn llm for ai."}],
    model="llama3.1-8b",
    max_completion_tokens=1024,
    temperature=0.2,
    top_p=1,
    stream=True
)

for chunk in response:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="")