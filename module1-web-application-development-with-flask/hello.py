"""Minimal flask app"""

from flask import Flask, render_template

#make the application
app = Flask(__name__)

#Make the route
@app.route("/")

#Now define a function
def hello():
    return "Hello World!"

#Make a second route
@app.route("/about")

#Now make a the function that goes with about
def preds():
    return render_template('about.html')