app = Flask(__name__)

@app.route("/hello")
>>>>>>> ad3529310c2fa7dfeea04429beb91895caad0bcb
     return render_template("index.html")


if __name__ == '__main__':
