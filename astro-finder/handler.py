import random
import requests


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    r = requests.get('https://api.open-notify.org/astros.json')
    result = r.json
    index = random.randint(0, len(result['people']) - 1)
    name = result['people'][index]['name']
    in_space = '{} is in space'.format(name)
    print(in_space)

    return in_space
