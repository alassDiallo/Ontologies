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
env = Environment()
g = Graph()
g.parse("ontology.ttl", format="ttl")
#onto = get_ontology("ontology.ttl")

# Définir les namespaces
seitoSMA = Namespace("http://www.owl-ontologies.com/seitoSMA#")
saref = Namespace("https://saref.etsi.org/core/v3.2.1/")
saref4bldg = Namespace("https://saref.etsi.org/saref4bldg/")

urlapi = "http://127.0.0.1:8000"
# response = requests.get(f"{urlapi}/donnees")
# print(response.json())"""
#sync_reasoner()

#retrieve the 
query = """
            PREFIX seitoSMA: <http://www.owl-ontologies.com/seitoSMA#>
            PREFIX saref4bldg: <https://saref.etsi.org/saref4bldg#>
            SELECT ?agent ?s
            WHERE {
                ?agent a seitoSMA:Agent .
                ?s a seitoSMA:Systéme .
                ?s seitoSMA:offers ?y .
              
            }
            
        """
#retrieve the HeatingAgentManagerSystems
heatingAgents = """
            PREFIX seitoSMA: <http://www.owl-ontologies.com/seitoSMA#>
            PREFIX saref4bldg: <https://saref.etsi.org/saref4bldg#>
            SELECT ?agent ?system ?device
            WHERE {
                ?agent a :HeatingAgentManager .
                ?system a :HeatingSystem .
                ?device a seitoSMA:Device .
                ?agent seitoSMA:manages ?system .
                ?device seitoSMA:isPartOf ?system .
                
            }
            
        """

#retrieve the lightingAgentManagerSystems
lightingAgents = """
            PREFIX seitoSMA: <http://www.owl-ontologies.com/seitoSMA#>
            PREFIX saref4bldg: <https://saref.etsi.org/saref4bldg#>
            SELECT ?agent ?system ?device
            WHERE {
                ?agent a :LightingAgentManager .
                ?system a :LightingSystem .
                ?device a seitoSMA:Device .
                ?agent seitoSMA:manages ?system .
                ?device seitoSMA:isPartOf ?system .
               
            }
            
        """
"""for subj, pred, obj in g:
    print(subj, pred, obj)"""
#create a dict to store the set of agents
dictAgent = dict()
resultLighting = g.query(lightingAgents)
"""
configuring the agent and the systems with the devices
"""
c = 1
for z in resultLighting:
    name_agent = z.agent.split("#")[1]
    agent_id = "LightingAgent" + str(c)
    #device = Device(id=z.device.split("#")[1])
    if any(agent.id == name_agent for agent in dictAgent.values()):
        print("agent existe")
        #agent.managedSystem.addDevice(device) 
    else:
        print(agent_id,"====> l'agent existe pas") 
        managedSystem = LightingSystem(z.system.split("#")[1])
        #managedSystem.addDevice(device)
        agent = LightingSystemAgentManager(id=name_agent,managedSystem=managedSystem)
        dictAgent[agent_id]=agent
        c = c+1
    if z.device is not None:
       device = Device(id=z.device.split("#")[1])
       agent.managedSystem.addDevice(device) 
    

result = g.query(heatingAgents)
c = 1
for z in result:
    name_agent = z.agent.split("#")[1]
    id = "HeatingAgent" + str(c)
    #device = Device(id=z.device.split("#")[1])
    if any(agent.id == name_agent for agent in dictAgent.values()):
        print("agent existe")
        #agent.managedSystem.addDevice(device) 
    else:
        print(agent_id,"====> l'agent existe pas") 
        managedSystem = HeatingSystem(z.system.split("#")[1])
        #managedSystem.addDevice(device)
        agent = HeatingSystemAgentManager(id=name_agent,mangedSysteme=managedSystem)
        dictAgent[id]=agent
        c = c+1
    if z.device is not None:
       device = Device(id=z.device.split("#")[1])
       agent.managedSystem.addDevice(device) 

#initialize the set of agent in the environment
env.setAgents=dictAgent
print("affichage des agents avec les appareils ")
#display the agent and the system they manages
for a in env.setAgents:
    print("########################### ",a," ###########################################")
    print(a," manages ",dictAgent[a].managedSystem, "and content ",len(dictAgent[a].managedSystem.devices)," devices")
    for d in dictAgent[a].managedSystem.devices:
        print(d)
    print("##############################################################################")













g = Graph()
        g.parse("ontology.ttl", format="ttl")
        #onto = get_ontology("ontology.ttl")

        # Définir les namespaces
        seitoSMA = Namespace("http://www.owl-ontologies.com/seitoSMA#")
        saref = Namespace("https://saref.etsi.org/core/v3.2.1/")
        saref4bldg = Namespace("https://saref.etsi.org/saref4bldg/")

        urlapi = "http://127.0.0.1:8000"
        # response = requests.get(f"{urlapi}/donnees")
        # print(response.json())"""
        #sync_reasoner()

        #retrieve the 
        query = """
                    PREFIX seitoSMA: <http://www.owl-ontologies.com/seitoSMA#>
                    PREFIX saref4bldg: <https://saref.etsi.org/saref4bldg#>
                    SELECT ?agent ?s
                    WHERE {
                        ?agent a seitoSMA:Agent .
                        ?s a seitoSMA:Systéme .
                        ?s seitoSMA:offers ?y .
                    
                    }
                    
                """
        #retrieve the HeatingAgentManagerSystems
        heatingAgents = """
                    PREFIX seitoSMA: <http://www.owl-ontologies.com/seitoSMA#>
                    PREFIX saref4bldg: <https://saref.etsi.org/saref4bldg#>
                    SELECT ?agent ?system ?device
                    WHERE {
                        ?agent a :HeatingAgentManager .
                        ?system a :HeatingSystem .
                        ?device a seitoSMA:Device .
                        ?agent seitoSMA:manages ?system .
                        ?device seitoSMA:isPartOf ?system .
                        
                    }
                    
                """

        #retrieve the lightingAgentManagerSystems
        lightingAgents = """
                    PREFIX seitoSMA: <http://www.owl-ontologies.com/seitoSMA#>
                    PREFIX saref4bldg: <https://saref.etsi.org/saref4bldg#>
                    SELECT ?agent ?system ?device
                    WHERE {
                        ?agent a :LightingAgentManager .
                        ?system a :LightingSystem .
                        ?device a seitoSMA:Device .
                        ?agent seitoSMA:manages ?system .
                        ?device seitoSMA:isPartOf ?system .
                    
                    }
                    
                """
        """for subj, pred, obj in g:
            print(subj, pred, obj)"""
        #create a dict to store the set of agents
        dictAgent = dict()
        resultLighting = g.query(lightingAgents)
        """
        configuring the agent and the systems with the devices
        """
        c = 1
        for z in resultLighting:
            name_agent = z.agent.split("#")[1]
            agent_id = "LightingAgent" + str(c)
            #device = Device(id=z.device.split("#")[1])
            if any(agent.id == name_agent for agent in dictAgent.values()):
                print("agent existe")
                #agent.managedSystem.addDevice(device) 
            else:
                print(agent_id,"====> l'agent existe pas") 
                managedSystem = LightingSystem(z.system.split("#")[1])
                #managedSystem.addDevice(device)
                agent = LightingSystemAgentManager(id=name_agent,managedSystem=managedSystem)
                dictAgent[agent_id]=agent
                c = c+1
            if z.device is not None:
                device = Device(id=z.device.split("#")[1])
                agent.managedSystem.addDevice(device) 
            

        result = g.query(heatingAgents)
        c = 1
        for z in result:
            name_agent = z.agent.split("#")[1]
            id = "HeatingAgent" + str(c)
            #device = Device(id=z.device.split("#")[1])
            if any(agent.id == name_agent for agent in dictAgent.values()):
                print("agent existe")
                #agent.managedSystem.addDevice(device) 
            else:
                print(agent_id,"====> l'agent existe pas") 
                managedSystem = HeatingSystem(z.system.split("#")[1])
                #managedSystem.addDevice(device)
                agent = HeatingSystemAgentManager(id=name_agent,mangedSysteme=managedSystem)
                dictAgent[id]=agent
                c = c+1
            if z.device is not None:
                device = Device(id=z.device.split("#")[1])
                agent.managedSystem.addDevice(device) 

        #initialize the set of agent in the environment
        self.setAgents=dictAgent