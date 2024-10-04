from bot.lib.register import register
from bot.lib.utils import press, write_confirm
from sys import argv

import json
import pyautogui

"""
from flask import Flask, request

api = Flask(__name__)


@api.route("/register", methods=["GET", "POST"])
def index():
    pass


api.run(host="0.0.0.0")
"""

if pyautogui.confirm(text="Tela do sistema", buttons=["Ok", "Cancel"]) == "Ok":
    with open(argv[1]) as fp:
        items: map = json.load(fp)

        for item in items:
            press("F2")
            write_confirm(item)
            register(items[item]["desc"], value_2=items[item]["value_2"])
            press("F10")

            if pyautogui.confirm(text="Next", buttons=["Ok", "Cancel"]) == "Ok":
                continue
            else:
                exit()
