from flask import Flask, render_template, jsonify, request
from werkzeug.utils import secure_filename
from PCFG import PCFG
from GUI import GUI
from os import getcwd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/getpcfg", methods=["POST"])
def getpcfg():
    if request.method == "POST":
        corpus = request.files["corpus-file"]
        corpus.save(getcwd() + "/upload/" + secure_filename(corpus.filename))

        pcfg = PCFG(secure_filename(corpus.filename))

        return jsonify(dict(send=True))



if __name__ == '__main__':
    # ui = GUI(app)
    # ui.run()
    app.run()