from flask import Flask, render_template, request
from bot.lib.register import register

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        register("Test", "00000001", 0, "00000000", "00000000")

    return render_template("index.html")


app.run(host="0.0.0.0")
