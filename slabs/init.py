from flask import Flask, render_template, request, session
import json
from generateCards import createWhiteCards, createBlackCards
from player import *
import random

app = Flask(__name__)

whiteCards = []
blackCards = []
players = []
turnCount = 0
gameMaster = None

@app.before_first_request
def activate():
    app.secret_key = "slabz"
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
    # TODO where does gameMaster go?
    return render_template("game.html", player=session['player'])


@app.route("/join", methods=['post'])
def join():
    global whiteCards
    type = request.form['type']
    name = request.form['name']
    if type == "join" and name != "":
        # user can join a game.
        player = Player(name)
        # get 4 cards for the player
        count = 0
        while count < 4:
            index = random.randint(0,len(whiteCards)-1)
            player.addCard(whiteCards[index])
            whiteCards.pop(index)
            count +=1
        players.append(player)
        # add player to session.
        session['player'] =json.dumps(player.__dict__)
        print("Player added: " + player.name)
        if len(players) == 1:
            return render_template("preGame.html", name=name, master="true")
        return render_template("preGame.html", name=name)
    elif type == "watch":
        # user can watch a game.
        return render_template("preGame.html")



if __name__ == '__main__':
    app.secret_key = "slabz"
    app.run()
