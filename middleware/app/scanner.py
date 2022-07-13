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
    scan_name = request.args.get("scan_name")
    working_directory = request.args.get("working_directory")
    if working_directory!=None or scan_name!=None:
        print(working_directory[0])
        cmd = "docker run --name "+scan_name+" -v "+str(working_directory)+":/project ort --info scan -i /project/analyzer-result.yml -o /scan"
        cmdList = cmd.split()
        try:
            p = subprocess.Popen(cmdList, cwd=working_directory,stdout=PIPE)
            p.wait()
            text = p.communicate()[0]
            print(text)
            return "success"
        except:
            return "an exception occurred"
    else:
        return "working directory and scan name can't be null!"


@app.route("/start")
def startScan():
    return render_template("scannerOptions.html")

@app.route("/listScans")
def listScans():
    pass 

@app.route("/stopScan")
def stopScan():
    pass

@app.route("/getScan")
def getScan():
    pass
