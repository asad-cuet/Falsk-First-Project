from flask import Flask,request,jsonify
import pandas as pd
import os
import json

from flask import send_file


app=Flask(__name__)

@app.route('/')
def index():
    data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
    }
    df = pd.DataFrame(data)
    return df.to_html()     # to_string(),to_dict(),to_json(0)

book_list=[
    {
        'id':1,
        'name':'asad',
        'author':'rahat'
    }
]    

@app.route('/books',methods=['GET'])
def books():
    return jsonify(book_list)


@app.route('/csv-read')
def data():
    df=pd.read_csv(os.path.abspath(os.getcwd())+"/made.csv",encoding='windows-1252')  # also 1254
    return df.to_json()


@app.route('/csv-download') # this is a job for GET, not POST
def plot_csv():
    return send_file(
        'made.csv',
        mimetype='text/csv',
        download_name='name.csv',
        as_attachment=True
    )