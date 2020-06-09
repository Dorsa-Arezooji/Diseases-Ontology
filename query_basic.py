import logging
import rdflib
from _pyio import open

logging.basicConfig()

query = """
PREFIX dis: <http://www.semanticweb.org/dorsa/ontologies/diseases.owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  
SELECT DISTINCT ?d_name ?c_name ?co_name
WHERE { ?d rdf:type dis:disease .
        ?d dis:name ?d_name .
        ?d dis:caused_by ?cause .
        ?cause rdf:type dis:environmental .
        ?cause dis:name ?c_name .
        ?d dis:outbreak_in ?country .
        ?country dis:name ?co_name .
      }"""

g=rdflib.Graph()
result=g.parse("diseases_populated_3.owl", "xml")
print("graph has %s statements.\n" % len(g))

print ('{0:25s} {1:20s} {2:10s}'.format("Environmental Disease","Cause", "Country"))
for x,y,z in g.query(query):
    print ('{0:25s} {1:20s} {2:10s}'.format(x,y,z))
