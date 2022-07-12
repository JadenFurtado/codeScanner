# the analysis module of the scanner

from app import app
from flask import Flask, make_response,jsonify
from flask import request,render_template
import subprocess
from subprocess import PIPE
import json
import docker
import mysql.connector

# the analysis page
@app.route("/analysis")
def analysisOPtions():
    return render_template("index.html")

@app.route("/analysis/list/all")
def analysisListAll():
    return render_template("getAnalysis.html")

@app.route("/startAnalysis")
def analyze():
    scan_name = request.args.get("scan_name")
    working_directory = request.args.get("working_directory")
    if working_directory!=None or scan_name!=None:
        print(working_directory[0])
        cmd = "docker run --name "+scan_name+" -v "+str(working_directory)+":/project ort --info analyze -i /project -o /scan"
        cmdList = cmd.split()
        try:
            mydb = mysql.connector.connect(host = app.config['DB_HOST'],user=app.config['DB_USERNAME'],password=app.config['DB_PASSWORD'],database=app.config['DB_NAME']) 
            mycursor = mydb.cursor()
            p = subprocess.Popen(cmdList, cwd=working_directory,stdout=PIPE)
            p.wait()
            text = p.communicate()[0]
            print(text)
            sql = "INSERT INTO analysis(containerId,scanPath) VALUES(%s,%s)"
            val = (scan_name,working_directory)
            mycursor.execute(sql,val)
            print(mycursor)
            mydb.commit()
            mydb.close()
            return "success"
        except:
            return "an exception occurred"
    else:
        return "working directory and scan name can't be null!"

""" @app.route("/listAnalysis")
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
    return json.dumps(listContainer) """

@app.route("/showAllAnalysis")
def showAllAnalysis():
    try:
        mydb = mysql.connector.connect(host = app.config['DB_HOST'],user=app.config['DB_USERNAME'],password=app.config['DB_PASSWORD'],database=app.config['DB_NAME']) 
        mycursor = mydb.cursor()
        sql = "SELECT * FROM analysis"
        mycursor.execute(sql)
        myres = mycursor.fetchall()
        rows = list()
        for row in myres:
            newRow = dict()
            newRow["id"] = row[0]
            newRow["name"] = row[1]
            newRow["path"] = row[2]
            rows.append(newRow)
        mydb.commit()
        mydb.close()
        resp = make_response(jsonify(rows))
        return resp
    except:
        return "an exception occurred"

@app.route("/stopAnalysis")
def stopAnalysis():
    pass

@app.route("/saveAnalysis")
def getAnalysis():
    testName = request.args.get("testName")
    resultDirectory = request.args.get("resultDirectory")
    if testName==None or resultDirectory==None:
        return "testName or result Directory cannot be null"
    try:
        cmd = 'docker ps -aqf name=^'+testName+'$'
        cmdList = cmd.split()
        working_directory = resultDirectory
        p = subprocess.Popen(cmdList, cwd=working_directory,stdout=PIPE)
        p.wait()
        containerId = str(p.communicate()[0],"UTF-8")
        cmd = "docker cp "+containerId.strip()+":/scan "+resultDirectory
        print(cmd)
        cmdList = cmd.split()
        p = subprocess.Popen(cmdList, cwd=working_directory,stdout=PIPE)
        p.wait()
        return "success"
    except:
        return "an error occurred"

@app.route("/fetchAnalysis")
def fetchAnalysis():
    return render_template("testFetchAnalysis.html")