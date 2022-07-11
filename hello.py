import http
from flask import Flask
from discord_bot import translator
from groupme import listener
app =Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>London 2.0</h1>"



@app.route('/groupme')
def groupme():
    testing = listener.getandgrab()
    print('working')


while True:
    groupme()
    
    