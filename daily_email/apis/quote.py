import requests


def get_quote():
    url = "https://quotes.rest/qod"

    headers = {
        'content-type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)

    quote = response.json()['contents']['quotes'][0]['quote']
    author = response.json()['contents']['quotes'][0]['author']
    text = f"{quote}\n\t\t~ {author}"
    return text.strip()


if __name__ == '__main__':
    print(get_quote())
