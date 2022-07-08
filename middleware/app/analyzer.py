# the analysis module of the scanner

from app import app
from flask import Flask
from flask import request,render_template
import subprocess
from subprocess import PIPE
import json
import docker

# the analysis page
@app.route("/analysis")
def analysisOPtions():
    return render_template("index.html")

@app.route("/startAnalysis")
def analyze():
    working_directory = request.args.get("working_directory")
    if working_directory!=None:
        print(working_directory[0])
        cmd = "docker run --name testin -v "+str(working_directory)+":/project ort --info analyze -i /project -o /scan"
        cmdList = cmd.split()
        p = subprocess.Popen(cmdList, cwd=working_directory,stdout=PIPE)
        p.wait()
        text = p.communicate()[0]
        print(text)
        return "success"
    else:
        return "working_directory can't be null!"

@app.route("/listAnalysis")
def listAnalysis():
    client = docker.from_env()
    f = open ('/home/jadenfurtado/Desktop/repoScanner/middleware/app/containers.json', "r")  
    data = json.loads(f.read())
    client = docker.from_env()
    listContainer  = list()
    for c in data['containers']:
        print(c['containerId'])
        containerStatus = dict()
        cont = client.containers.get(c['containerId'])
        containerStatus['conainterId'] = c['containerId']
        containerStatus['status'] = cont.attrs['State']['Status']
        listContainer.append(containerStatus)
    return json.dumps(listContainer)

@app.route("/stopAnalysis")
def stopAnalysis():
    pass

@app.route("/getAnalysis")
def getAnalysis():
    pass
