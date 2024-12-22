import os
import json
import requests
from dotenv import load_dotenv  

load_dotenv()

# Define the URL for the Ollama server
# url = "http://windows-host:11434/api/generate"
# url = "http://localhost:11434/api/generate"
# Create the data payload with the model and prompt

data = {
    "model": "llama3.2",
    "prompt": "Why is the sky blue?"
}

url = os.environ['WINDOWS_HOST']+'/api/generate'
# url = os.environ['WSL_HOST']+'/api/generate'

# Make the POST request to the Ollama server
response = requests.post(url, json=data, stream=True)

# Check the response status
if response.status_code == 200:
    print("Generated text:", end=" ", flush=True)
    for chunk in response.iter_lines():
        if chunk:
            decoded_chunk = chunk.decode("utf-8")
            result = json.loads(decoded_chunk)
            generated_text = result.get("response", "")
            print(generated_text, end="", flush=True)
else:
    print("Error", response.status_code, response.text)