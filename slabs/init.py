from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def main():
    print("hello")


if __name__ == '__main__':
    main()
