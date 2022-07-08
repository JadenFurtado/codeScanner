# the scanner module of the scanner

from app import app
from flask import Flask
from flask import request,render_template
import subprocess
from subprocess import PIPE
import json
import docker

# the analysis page
@app.route("/scanner")
def scannerOptions():
    pass

@app.route("/startScan")
def startScan():
    pass

@app.route("/listScans")
def listScans():
    pass 

@app.route("/stopScan")
def stopScan():
    pass

@app.route("/getScan")
def getScan():
    pass
