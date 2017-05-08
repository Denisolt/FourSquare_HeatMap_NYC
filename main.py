import os,csv
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

import pandas as pd

#data = pd.read_csv('data.csv')
#location = data.latitude.astype(str) + ", " + data.longitude.astype(str)
#print location

app = Flask(__name__)

@app.route('/')
def index():
    data = pd.read_csv('data.csv')
    location = data.latitude.astype(str) + ", " + data.longitude.astype(str)
    return render_template('index.html', x = location)


if __name__ == '__main__':
   app.run(debug = True, port=33507)
