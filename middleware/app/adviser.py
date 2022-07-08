# the analysis module of the scanner

from app import app
from flask import Flask
from flask import request,render_template
import subprocess
from subprocess import PIPE
import json
import docker

# the analysis page
@app.route("/adviser")
def adviserOptions():
    return render_template("index.html")

@app.route("/startAdviser")
def startAdviser():
    pass 

@app.route("/listAdvisories")
def listAdvisories():
    pass

@app.route("/stopAdvisories")
def stopAdvisories():
    pass

@app.route("/getAdvisories")
def getAdvisories():
    pass
