import requests
from environs import Env

env = Env()
env.read_env()
api_key = env('HF_API_KEY')

def query_huggingface_ai(prompt, model="meta-llama/Llama-3.2-3B-Instruct"):
    API_URL = "https://router.huggingface.co/v1/chat/completions"

    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "model": model
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]


def get_quote():
    prompt = "Give me a new (one you haven't told me yet), real, short, and inspiring quote or mantra for the day. Just give me the quote and who said it, no extra text."

    content = query_huggingface_ai(prompt)

    if content:
        return content['content']
    else:
        return "Every day is a new opportunity to grow and learn. Embrace today's challenges with courage and curiosity."


if __name__ == "__main__":
    print(get_quote())