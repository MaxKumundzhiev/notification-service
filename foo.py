import requests

from json import dumps


def generate():
    import string
    from random import choices

    N = 10
    text = ''.join(choices(string.ascii_uppercase + string.digits, k=N))
    return {"raw": text}


for _ in range(100):
    address = "http://0.0.0.0:8000/messages"
    raw = generate()
    r = requests.post(url=address, json=raw)
    print(r.status_code)




