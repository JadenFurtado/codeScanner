import json
import docker

client = docker.from_env()
cont = client.containers.get("7df739ae40a0")

print(cont.attrs['State']['Status'])
f = open ('/home/jadenfurtado/Desktop/repoScanner/middleware/app/containers.json', "r")  
data = json.loads(f.read())
client = docker.from_env()
listContainer  = list()
for c in data['containers']:
    print(c['containerId'])
    cont = client.containers.get(c['containerId'])
    containerStatus['conainterId'] = cont.attrs['State']['Status']
    print(cont.attrs['State']['Status'])
""" for c in data['containers']:"""
