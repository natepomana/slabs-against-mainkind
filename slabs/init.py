from flask import Flask, render_template, request
import json
app = Flask(__name__)

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
    if type == "join" && name != "":
        # user can join a game.
        return
    elif type == "watch":
        # user can watch a game.
        return
    return name


if __name__ == '__main__':
    app.run()
