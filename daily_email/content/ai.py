import os
import requests

API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {os.environ['HF_API_KEY']}",
}

messages = []

def query(prompt):
    messages.append({
                "role": "user",
                "content": prompt,
            })
    payload = {
        "messages": messages,
        "model": "meta-llama/Llama-3.2-3B-Instruct:together"
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    message_response = response.json()["choices"][0]["message"]
    messages.append(message_response)
    return message_response['content']


def get_mantra():
    prompt = "Give me another short daily mantra to start my day, without an intro or explanation. Just max 10 words."
    return query(prompt).strip('"')

if __name__ == '__main__':
    print(get_mantra())
    print(get_mantra())
    print(get_mantra())
    print(get_mantra())