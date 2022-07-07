import http
from flask import Flask
from discord_bot import translator
from flask import Request
app =Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>London 2.0</h1>"



@app.route('/groupme')
def groupme():
    pass