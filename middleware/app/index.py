from app import app
from flask import Flask
from flask import request,render_template

@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

