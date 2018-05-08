import random
import requests


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    print(req)
    url = 'http://api.open-notify.org/astros.json'
    print('Grabbing astros from url {}'.format(url))
    r = requests.get(url)
    result = r.json()
    print('Got result {}'.format(result))
    index = random.randint(0, len(result["people"]) - 1)
    name = result["people"][index]["name"]
    in_space = '{} is in space'.format(name)
    print(in_space)

    return in_space
