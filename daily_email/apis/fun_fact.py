import requests


def get_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    headers = {
        'content-type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)
    response.raise_for_status()

    data = response.json()
    joke = data['text']

    return joke.strip()


if __name__ == '__main__':
    print(get_fact())
