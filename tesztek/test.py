from hom import *
from figyelo_1 import *
from flask import Flask
from flask import jsonify
import time




app = Flask(__name__)

@app.route("/")

def ertek():
    try:
        time.sleep(5)
        return jsonify(homerseklet = loopi())
    
    except AttributeError:
        print("Valami szar")
        pass