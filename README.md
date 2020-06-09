# Diseases-Ontology
An ontology for human diseases

## Overview
The goal is to first create an ontology with relevant classes and properties, `diseases_rdf.owl`, and then populate it using one (`basic.py`, `basic1.py`, `basic2.py`) or multiple (`bonus.py`) online databases.

## Usage
A use case for this ontology is to query the ontology for the symptoms someone might be showing and get back a list of possible diseases that could cause that collection of symptoms. Another use case might be to get a list of diseases related to a certain type of cause (genetic, infectious, environmental).
There are so many fields of medical specialties and it would be impossible for one to be an expert on all of them. Also, there are a large number of rare diseases that might be missed by even specialists. This concept could be a useful tool for doctors to make sure not to miss any possible explanations in differential diagnoses.

## Data
The database chosen for this project is `Wikidata` since it is well-structured (the properties are actually defined for a large number of diseases) and has a perfectly decent working endpoint. The only drawback is that terms (classes, properties, etc.) are defined using identifiers and should be referred to as such while querying the database.

* [infectious diseases](http://www.wikidata.org/entity/Q18123741)

* [environmental diseases](http://www.wikidata.org/entity/Q3751709)

* [genetic diseases](http://www.wikidata.org/entity/Q200779)

The second source chosen for the bonus part is `dbpedia`, which is used to populate the ontology created in the basic part.

* [death cause of famous people](http://dbpedia.org/ontology/deathCause)

## Code
There are three types of disease causes: infectious, genetic, environmental. Since querying all of these in one sparql query results in server timeout, a different approach is taken: chaining multiple queries.
First, all the infectious diseases are queried and used to populate the ontology. The output file is saved and used as input to the second query, which queries all the environmental diseases. Finally the last query populates the ontology with genetic diseases.

### Ontology
The structure of the ontology:

    Classes                                   Object Properties                          Data Properties     

![ontology structure](https://github.com/Dorsa-Arezooji/Diseases-Ontology/blob/master/ontology_structure.png)

### Populate
The codes should be run in this order:
1. `basic.py` → populates the ontology with infectious disease form `wikidata`
2. `basic1.py` → populates the ontology with environmental disease form `wikidata`
3. `basic2.py` → populates the ontology with genetic disease form `wikidata`
4. `bonus.py` → as the second source of data, uses `dbpedia` to populate the ontology by adding the
names of famous people whose cause of death was *pneumonia*

The populated ontologies after each step are included in [populated models](https://github.com/Dorsa-Arezooji/Diseases-Ontology/tree/master/populated_models).

### Query
query_basic.py → queries for environmental diseases and related info

__*Results:*__

```
Environmental Disease     Cause           Country
itai-itai disease         cadmium         Japan
Yokkaichi asthma          air pollution   Japan
Niigata Minamata disease  mercury         Japan
```
