from urllib import response
import requests
import json

url = "http://localhost:11434/api/generate"

data ={
    "model": "llama3.2",
    "prompt": "What is the capital of France?",
}

response = requests.post(url, json=data, verify=False, stream=True)

# Check if the request was successful
if response.status_code == 200:
    # Process the response stream
    for chunk in response.iter_lines():
        if chunk:
            # Decode the chunk and print it
            decoded_chunk = chunk.decode('utf-8')
            result = json.loads(decoded_chunk)
            #Get text from text
            generated_text = result.get("response", "")
            print(generated_text,end="",flush=True)
else:
    print(f"Request failed with status code: {response.status_code}")
    print("Response content:", response.text)