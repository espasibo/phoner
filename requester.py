import requests

def getdom(url):
    line = requests.get(url)
    return line.text
