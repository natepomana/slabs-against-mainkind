class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def playCard(self, id):
        card = self.cards[id]
        self.cards.pop(id)
        return card

    def getCards(self):
        return self.cards

    def addCard(self, card):
        self.cards.append(card)
