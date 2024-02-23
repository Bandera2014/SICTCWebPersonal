from flask import Flask, request, redirect, url_for, jsonify, Blueprint, send_file, make_response
from flask_cors import CORS
import pymysql

from routes import States, Accounts

app = Flask(__name__)
CORS(app)

#put all of the db connection material in separate class
import sys                  #GPT this, needed to put the eonnection stuff in separate file
sys.path.append('routes/')  
from DBConnection import connectToDB
#Typically this would be with the imports, but here for learning
connection=connectToDB()

@app.route('/')
def hello():
    return "up and running"

app.register_blueprint(States.stateBP,url_prefix='/states/')
app.register_blueprint(Accounts.accountBP,url_prefix='/accounts/')

app.run(debug=True,host="0.0.0.0",port=3000)
