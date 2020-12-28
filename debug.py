import json

with open('info.json', 'r') as fi:
        data = json.loads(fi.read())
    ficnt = data