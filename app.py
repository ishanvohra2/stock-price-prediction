import pandas as pd
from flask import Flask, jsonify, request
from tensorflow.keras.models import load_model
import pickle
import numpy as np

MODEL = load_model('SavedModel')

# app
app = Flask(__name__)

# routes
@app.route('/tesla/', methods=['POST'])

def predict()
    # get data
    data = request.get_json(force=True)
    

