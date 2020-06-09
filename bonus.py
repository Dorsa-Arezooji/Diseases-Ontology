import logging
import rdflib
from rdflib import Graph, URIRef
from SPARQLWrapper import SPARQLWrapper, RDF
from rdflib.plugins.memory import IOMemory

logging.basicConfig()
 
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
construct_query="""
      PREFIX dis: <http://www.semanticweb.org/dorsa/ontologies/diseases.owl#>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
      PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX wd: <http://www.wikidata.org/entity/>
      
      CONSTRUCT {
      ?d rdf:type dis:disease .
      ?d dis:name ?dLabel.
      ?d dis:cause_of_death_of ?p .
      ?p rdf:type dis:person .
      ?p dis:name ?pLabel .
      
      }
       WHERE{
       ?d rdf:type dbpedia-owl:Disease .
       ?d owl:sameAs wd:Q12192 .
       ?d rdfs:label ?dLabel .
       ?p rdf:type dbpedia-owl:Person .
       ?p dbpedia-owl:deathCause ?d .
       ?p rdfs:label ?pLabel .
       FILTER (langMatches(lang(?dLabel), "en")) .
       FILTER (langMatches(lang(?pLabel), "en")) .
       }"""

sparql.setQuery(construct_query)
sparql.setReturnFormat(RDF)


memory_store=IOMemory()
graph_id=URIRef('http://www.semanticweb.org/store/movie')
g = Graph(store=memory_store, identifier=graph_id)
rdflib.plugin.register('sparql', rdflib.query.Processor, 'rdfextras.sparql.processor', 'Processor')
rdflib.plugin.register('sparql', rdflib.query.Result, 'rdfextras.sparql.query', 'SPARQLQueryResult')
 
g = sparql.query().convert()
g.parse("diseases_populated_3.owl")
g.serialize("diseases_populated_4.owl", "xml")
