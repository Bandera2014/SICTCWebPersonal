from flask import Flask, Blueprint
from routes import Accounts
from routes import DBConnection


app = Flask(__name__)
app.register_blueprint(Accounts.accountBP,url_prefix="/accounts/")
# DBConnection.connectToDB()


@app.route('/')
def hello():
    return "up and running"

app.run(debug=True, host="0.0.0.0",port=3000)