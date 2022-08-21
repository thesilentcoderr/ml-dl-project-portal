# from crypt import methods
import numpy as np
from flask import Flask, request, jsonify, render_template
#DATA SCIENCE
from PIL import Image, ImageOps
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import tensorflow as tf
from keras.preprocessing import image
from keras.models import load_model
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def home():
    
    return render_template("index.html")

#------------------------------ML-------------------------------------------
@app.route('/ml', methods=["GET","POST"])
def ml():
    return render_template("ml.html")

#------------------------------DL-------------------------------------------
@app.route('/dl', methods=["GET","POST"])
def dl():
    return render_template("dl.html")

#------------------------------pre-process-------------------------------------------
@app.route('/pre-process', methods=["GET","POST"])
def pre_process():
    return render_template("pre-process.html")

#------------------------------About Me-------------------------------------------
@app.route('/about')
def aboutusnew():
    return render_template('aboutusnew.html')

if __name__ == "__main__":
    app.run(debug=True)