from flask import Flask, send_from_directory

app = Flask(__name__)


@app.get("/")
def home():
    return send_from_directory(app.root_path, "arcade.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
