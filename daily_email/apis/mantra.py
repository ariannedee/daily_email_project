from pprint import pprint

import requests
from environs import Env

DEBUG = False

env = Env()
env.read_env()

api_url = "https://router.huggingface.co/v1/chat/completions"

headers = {"Authorization": f"bearer {env('HF_API_KEY')}"}

payload = {
        "messages": [
            {
                "role": "user",
                "content": "Give me a daily mantra that's 10 words or less",
            }
        ],
        "model": "Qwen/Qwen2.5-7B-Instruct:together"
    }
response = requests.post(api_url, headers=headers, json=payload)

response.raise_for_status()

data = response.json()

if DEBUG:
    pprint(data)

message = data["choices"][0]["message"]
daily_mantra = message["content"]

if __name__ == "__main__":
    print(daily_mantra)
