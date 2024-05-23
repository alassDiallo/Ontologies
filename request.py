import requests
#import json
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.tools.rdf2dot import rdf2dot
import sys
#from owlready2 import *

# Générer le fichier DOT à partir du graphique RDF



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
"""for subj, pred, obj in g:
    print(subj, pred, obj)"""
result = g.query(heatingAgents)
for z in result:
    print(z.agent,"manages => ",z.system, "=> contains device => ",z.device)

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
