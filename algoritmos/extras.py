import urllib, json

def leer_json(url):
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data