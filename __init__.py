import pcfg
from GUI import GUI
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


if __name__ == '__main__':
    ui = GUI(app)
    ui.run()