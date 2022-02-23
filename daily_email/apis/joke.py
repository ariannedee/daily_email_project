import requests


def get_joke():
    url = "https://api.jokes.one/jod"

    headers = {
        'content-type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)

    joke = response.json()['contents']['jokes'][0]['joke']['text']

    return joke.strip()


if __name__ == '__main__':
    print(get_joke())
