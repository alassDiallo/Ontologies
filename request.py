import requests
#import json
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.tools.rdf2dot import rdf2dot
import sys
from agents.HeatingSystemAgentManager import HeatingSystemAgentManager
from agents.LightingSystemAgentManager import LightingSystemAgentManager
from systems import *
from systems.HeatingSystem import HeatingSystem
from systems.LightingSystem import LightingSystem
from devices.Device import *
from environment import *
#from owlready2 import *

# Générer le fichier DOT à partir du graphique RDF

def requestData(setAgents):

    # rdf2dot(g, sys.stdout)

    # login URL login_url = "https://ellonasoft.io/api/v2/login"
    # data extraction URL data_url = "https://ellonasoft.io/api/v2/extract-data"
    # data to sent to API
    # login URL 
    #login_url = "https://ellonasoft.io/api/v2/login"
    # data extraction URL 
    """data_url = "https://ellonasoft.io/api/v2/extract-data"
    body_login = {"login": "AAcolant","password":"jidFZE)_XSd1"}
    body_data = {'from': '2024-05-18T10:49:05Z',
    'to': '2024-05-18T10:51:05Z',
    'sources': ['POD2-00335'],
    'types': ['temperature','humidity']
    }"""
    # sending post request and saving response as response object
    """r_login = requests.post(url=login_url, json=body_login)
    print('login retrieval status: %s' % r_login.status_code)
    if(r_login.status_code == 200):
        json = r_login.json()
        token = json['token']
        print('token: %s' % token)
        r_data = requests.post(url=data_url,json=body_data,headers={'x-auth':token})
        print('data retrieval status: %s' % r_data.status_code)
        if(r_data.status_code == 200):
            print(r_data.json())"""

    """heatingAgent = HeatingSystemAgentManager()
    print(heatingAgent)
    print(heatingAgent.preferenceTemperature)
    heatingAgent.increasePreferedTemperature()
    print(heatingAgent.preferenceTemperature)
    heatingAgent.decreasePreferedTemperature()
    print(heatingAgent.preferenceTemperature)
    heatingAgent.automationRegulatiopn(10)
    heatingAgent.automationRegulatiopn(40)
    """
    login_url = "https://ellonasoft.io/api/v2/login"
    data_url = "https://ellonasoft.io/api/v2/extract-data"
    # data to sent to API
    body_login ={'login': 'AAcolant','password':'jidFZE)_XSd1'}
    body_data = {
    "from": "2024-05-23T12:20:05Z",
    "to": "2024-05-23T12:25:10Z",
    "types":["temperature","humidity"]
    }
    # sending post request and saving response as response object
    r_login = requests.post(url=login_url, json=body_login,verify=False)
    print('login retrieval status: %s' % r_login.status_code)
    if(r_login.status_code == 200):
        json = r_login.json()
        token = json['token']
        print('token: %s' % token)
        r_data = requests.post(url=data_url,json=body_data,headers={'x-auth':token},verify=False)
        print('data retrieval status: %s' % r_data.status_code)
        if(r_data.status_code == 200):
            print(r_data.json())
            r=r_data.json()["data"]
            print("la date est : ",r["measurements"][0]['date'])
            print(r["devices"])
            for d in r["devices"]:
                print(r["devices"][d])
                for agent in [ agent for agent in setAgents if setAgents[agent].managedSystem is not None]:
                    if r["devices"][d] in setAgents[agent].managedSystem.devices:
                        print("device found ",r["devices"][d]," system ",setAgents[agent].managedSystem)
                        device = Device(id=r["devices"][d])
                        for t in r["measurements"][0]:
                            if d == t.split("-")[0]:
                                types = r["types"][t]
                                #print(types)
                                if types =="humidity":
                                    hum=r["measurements"][0][t]
                                
                                elif types=="temperature":
                                    temp=r["measurements"][0][t]
                        print(temp,hum)
                        device = Device(id=r["devices"][d],hum=hum,temp=temp)
                        print(device)
                        setAgents[agent].automationRegulation(device)
                        break
                    else:
                        continue
                
                #types = [ t for t in r["measurements"][0] if d == t.split("-")[0]]
                #print(types)"""