import requests,json

def configureKeys(path):
    with open(path) as f:
        data = json.load(f)
    return data
path = r"test.json"
jsonBody = configureKeys(path)

r = requests.post('https://livepeer.com/api/stream',
                headers={'Content-type': 'application/json',
                'Authorization': 'Bearer 73b42c46-3f1c-464c-a48f-6ce7d6fe2855'},
                json=jsonBody)

print(r.json())
