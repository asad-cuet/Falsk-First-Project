from flask import Flask,request,jsonify
import pandas as pd
app=Flask(__name__)

@app.route('/')
def index():
    data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
    }
    df = pd.DataFrame(data)

    # df.to_csv('made.csv')
    # df=pd.read_csv('liver.csv')
    return df.to_html()

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