import json

def debugmode(data):

    with open('info.json') as fi:
        data = json.loads(fi.read())
    return data

ficnt = debugmode([0])