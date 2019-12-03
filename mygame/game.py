from flask import Flask, escape, request, json, render_template, request
import random
import sys

app = Flask(__name__)

@app.route('/game') 
def index():
    return render_template("game.html")

if __name__ == "__main__":
    app.run()
