from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def main():
    return "Hello"


if __name__ == '__main__':
    main()
