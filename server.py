from flask import Flask

PORT = 8000
MESSAGE = "a = 33b = 200if b > a:print("b is greater than a")"

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
