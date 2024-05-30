from agents.AirQualitySystemAgentManager import AirQualitySystemAgentManager
from agents.MyAgent import MyAgent
import requests
#import json
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.tools.rdf2dot import rdf2dot
import sys
from agents.HeatingSystemAgentManager import HeatingSystemAgentManager
from agents.LightingSystemAgentManager import LightingSystemAgentManager
from systems import *
from owlready2 import *
from systems.AirQualitySystem import AirQualitySystem
from systems.HeatingSystem import HeatingSystem
from systems.LightingSystem import LightingSystem
from devices.Device import *
from environment import *
from systems.System import System
class Environment():
    def __init__(self):
        self.temperatureGloba=19
        self.setAgents = []


    def addAgent(self, agent:MyAgent):
        self.setAgents.append(agent)

    def configEnv(self):
        onto = get_ontology("TestF.rdf").load()
        print("Affichage des agents gestionnaire de chauffage")
        print(list(onto.classes()))
        seitoSMA = get_namespace("http://www.owl-ontologies.com/seitoSMA#")
        saref = get_namespace("https://saref.etsi.org/core/v3.2.1/")
        saref4bldg = get_namespace("https://saref.etsi.org/saref4bldg/")
        dictAgent = dict()

        with onto:
            sync_reasoner(infer_property_values = True)
            #is_a to get both subclass and idividuals
            #type to get individuals of a classe
            #iri to get an specifique object
            #subclass_of to get the subclasses of a classe
            #search_one to get only one element
        c=1
        for agent in onto.search(type=seitoSMA.Agent):
            print("#############################################################")
            print(agent," type ",agent.is_a)

            if agent.is_a[0] == onto.AirQualityAgentManager:
                name_agent = agent.name
                agent_id = "AirQualityAgent" + str(c)
                ag = AirQualitySystemAgentManager(id=name_agent)
                print("air quality agent manager",name_agent)
            
            elif agent.is_a[0] == onto.HeatingAgentManager:
                name_agent = agent.name
                agent_id = "HeatingAgent" + str(c)
                ag = HeatingSystemAgentManager(id=name_agent)
                print("heating agent manager",name_agent)
               
            elif agent.is_a[0] == onto.LightingAgentManager:
                name_agent = agent.name
                agent_id = "LightingAgent" + str(c)
                ag = LightingSystemAgentManager(id=name_agent)
                print("lighting agent manager",name_agent)
                print("lighting agent manager")
                
            else:
                name_agent = agent.name
                agent_id = "Agent" + str(c)
                ag = MyAgent(id=name_agent)
            location=None
            if hasattr(agent,"locatedIn") and len(agent.locatedIn)>0 :
                print(agent.locatedIn[0].name)
                location = agent.locatedIn[0].name

            if hasattr(agent,'manages') and len(agent.manages)>0:
                sysmanged = agent.manages
                #if len(sysmanged)>0:
                print("manager un systeme par un agent")
                sys=sysmanged[0]
                print("# ",sys," #")

                if sys.name is onto.HeatingSystem:
                    managedSystem = HeatingSystem(sys.name)
                elif sys.name is onto.LightingSystem:
                    managedSystem = LightingSystem(sys.name)
                elif sys.name is onto.AirQualitySystem:
                    managedSystem = AirQualitySystem(sys.name)
                else :
                    managedSystem = System(sys.name)
                #managedSystem.addDevice(device)
                #agent = HeatingSystemAgentManager(id=name_agent,mangedSysteme=managedSystem)
                if hasattr(sys,"hasDevice") and len(sys.hasDevice)>0:
                    #if len(sys.hasDevice)>0:
                    for d in sys.hasDevice:
                        device = Device(id=d.name)
                        managedSystem.addDevice(device) 
                    print("system with divice")
                    print(sys.hasDevice)
                    ag.managedSystem = managedSystem
                    ag.location = location

            if any(agent.id == name_agent for agent in dictAgent.values()):
                print("agent existe")
            else:
                print("existe pas")
                dictAgent[agent_id]=ag
                c+=1
            print("#############################################################")
        self.setAgents=dictAgent

    def __str__(self):
        #print("affichage des agents avec les appareils ")
        #display the agent and the system they manages*
        stre = "affichage des agents avec les appareils \n"
        for a in self.setAgents:
            #print(self.setAgents[a].managedSystem)
            stre +="########################### "+a+" location ===> "+ (self.setAgents[a].location+" " if self.setAgents[a].location is not None else "no location") +" ########################################### \n"
            #"+str(len(self.setAgents[a].managedSystem.devices))+"
            manage =  self.setAgents[a].id+ ((" manages "+str(self.setAgents[a].managedSystem)+" and content  devices "+str(len(self.setAgents[a].managedSystem.devices))+" \n" if self.setAgents[a].managedSystem.devices else " \n") if self.setAgents[a].managedSystem != None else " no system to manage \n")
            stre +=manage
            #stre += a+" manages "+ str(self.setAgents[a].managedSystem) + " and content  devices \n"
            if self.setAgents[a].managedSystem is not None:
                for d in self.setAgents[a].managedSystem.devices:
                    stre += str(d)+"\n"
            stre += "############################################################################## \n"

        return stre
    
    