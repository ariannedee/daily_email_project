import os
import requests

API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {os.environ['HF_API_KEY']}",
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

response = query({
    "messages": [
        {
            "role": "user",
            "content": "Give me a daily mantra, max 20 words"
        }
    ],
    "model": "Qwen/Qwen2.5-7B-Instruct:together"
})

mantra = response["choices"][0]["message"]["content"]

if __name__ == '__main__':
    print(response["choices"][0]["message"])
