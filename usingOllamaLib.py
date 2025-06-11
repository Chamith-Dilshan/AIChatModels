import re
from urllib import response
import ollama

# get the list of models
# response = ollama.list()
# print(response)

# chat example
res = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Why is the ocean is blue?"},
    ],
    stream=True,
)
#print(res)
#print(res["message"]["content"])
for chunk in res:
    if "message" in chunk:
        content = chunk["message"]["content"]
        if content:
            print(content, end="", flush=True)