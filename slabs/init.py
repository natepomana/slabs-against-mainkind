from flask import Flask, render_template, request
from generateCards import createWhiteCards, createBlackCards
from player import *
import random

app = Flask(__name__)

whiteCards = []
blackCards = []
players = []
gameMaster = None

@app.before_first_request
def activate():
    global whiteCards
    global blackCards
    whiteCards = createWhiteCards()
    blackCards = createBlackCards()
    print("Cards Generated.")


@app.route("/hello")
def home():
     return render_template("index.html")

@app.route("/game")
def game():
    # assign first person to gameMaster
    #gameMaster = players[0]
    wc = list()
    bc = blackCards[random.randint(0, len(blackCards))]
    wc.append(whiteCards[random.randint(0, len(whiteCards))])
    wc.append(whiteCards[random.randint(0, len(whiteCards))])
    wc.append(whiteCards[random.randint(0, len(whiteCards))])
    wc.append(whiteCards[random.randint(0, len(whiteCards))])
    return render_template("game.html", arr=wc, bc=bc)


@app.route("/join", methods=['post'])
def join():
    type = request.form['type']
    name = request.form['name']
    if type == "join" and name != "":
        # user can join a game.
        player = Player(name)
        player.getCards()
        players.append(player)
        print("Player added: " + player.name)
        if len(players) == 1:
            return render_template("preGame.html", name=name, master="true")
        return render_template("preGame.html", name=name)
    elif type == "watch":
        # user can watch a game.
        return render_template("preGame.html")



if __name__ == '__main__':
    activate()
    app.run()
