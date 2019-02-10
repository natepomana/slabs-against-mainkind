from flask import Flask, render_template, request
from generateCards import createWhiteCards, createBlackCards
app = Flask(__name__)

whiteCards = []
blackCards = []
players = []
gameMaster = ""

@app.before_first_request
def activate():
    whiteCards = createWhiteCards()
    blackCards = createBlackCards()
    print(whiteCards[2])
    print(blackCards[2])


@app.route("/hello")
def home():
     return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html")


@app.route("/join", methods=['post'])
def join():
    type = request.form['type']
    name = request.form['name']
    if type == "join" and name != "":
        # user can join a game.
        players.append(name)
        if players.count() == 1:
            return render_template("preGame.html", name=name, master=true)
        return render_template("preGame.html", name=name)
    elif type == "watch":
        # user can watch a game.
        return render_template("preGame.html")



if __name__ == '__main__':
    activate()
    app.run()
