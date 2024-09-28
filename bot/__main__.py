from flask import Flask, render_template, redirect
from bot.lib.fiscal import fiscal as fiscal_action

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/fiscal")
def fiscal():
    fiscal_action()
    return redirect("/")


app.run(host="0.0.0.0")
