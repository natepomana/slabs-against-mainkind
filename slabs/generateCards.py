import json


def createWhiteCards():
    with open('white.json', encoding='utf-8') as file:
        raw = json.loads(file.read())
    # go through each element and add the string
    data = []
    for card in raw:
        if card['rule'] == None:
            data.append(card['text'])
    return data

def createBlackCards():
    with open('black.json', encoding='utf-8') as file:
        raw = json.loads(file.read())
    # go through each element and add the string
    data = []
    for card in raw:
        if card['rule'] == None:
            data.append(card['text'])
    return data
