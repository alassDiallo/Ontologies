import requests
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.tools.rdf2dot import rdf2dot
import sys

# Générer le fichier DOT à partir du graphique RDF


g = Graph()
g.parse("C:\\Users\\Assane\\Desktop\\Ontologies\\DernierOntologieTest.ttl", format="ttl")

# Définir les namespaces
seitoSMA = Namespace("http://www.owl-ontologies.com/seitoSMA#")
saref = Namespace("https://saref.etsi.org/core/v3.2.1/")
saref4bldg = Namespace("https://saref.etsi.org/saref4bldg/")

urlapi = "http://127.0.0.1:8000"
# response = requests.get(f"{urlapi}/donnees")
# print(response.json())

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
"""for subj, pred, obj in g:
    print(subj, pred, obj)"""
result = g.query(query)
for z in result:
    print(z.agent, z.s)

# rdf2dot(g, sys.stdout)
