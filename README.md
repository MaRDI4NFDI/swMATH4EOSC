# swMATH and FairCore4Eosc

# WP7 The Mathematics Case Study

Adopted components


##  EOSC Data Type Registry (DTR) 

* Mathematics Subject Classification (MSC https://zbmath.org/classification/) should be added as a domain-specific data type to DTR
* Mathematics, in particular, LaTeX source code in titles as a domain-specific special case of the horizontal title field. Examples https://zbmath.org/1497.14042 and https://arxiv.org/abs/2004.08860 https://www.sciencedirect.com/science/article/abs/pii/S0021869321003021?via%3Dihub https://zbmath.org/7707391 https://zbmath.org/7658943 https://zbmath.org/7594811. Possible general alternatives are Title as HTML, Title as Image,
* What is currently in DTR that should be adopted by swMATH or zbMATH Open

##  EOSC Metadata Schema and Crosswalk Registry (MSCR)

The  EOSC Metadata Schema and Crosswalk Registry (MSCR) aims to support the publishing, discovery, and access of metadata schemata and provides functions to operationalize metadata conversions by combining crosswalks. Through the new API, research software programs and their metadata will be easily accessible, in particular via the CodeMeta standard. This component will be exposed so that one can use it to convert metadata of mathematical research software to ease the querying process.

Status: We can deposit codemeta files in SWH.

What is the schema, and what is the crosswalk?

schema: codemeta
crosswalk: mapping from swMATH internal data model to codemeta (link to github issue)

todo add the swMATH mapping between swMATH and CodeMeta to the crosswalk registry.


 ## EOSC Persistent Identifier Graph (PIdGraph)
Moreover, swMATH will integrate into the EOSC PIDGraph, which improves the way of interlinking research entities across domains and data sources based on PIDs (Persistent Identifiers); this can play a crucial role in helping applied mathematicians to identify the most convenient mathematical research software programs.

 ## EOSC PID Meta Resolver (PIMDR).
Standardized access to swMATH data is provided by integrating swMATH in the EOSC PID Meta Resolver (PIMDR)


##  Research Activity Identifier (RAiD) 
Research projects in Mathematics and indentified with a Research Activity Identifier (RAiD) should be harvestable through the PIDGraph API. These RAiDs must be linked with other PIDs like ORCID and DOIs.



## EOSC Research Discovery Graph (RDGraph)
Eventually, links between software and publications will also be discoverable via the EOSC Research Discovery Graph (RDGraph), which ensures that whenever a paper associated with a software that is indexed in swMATH is found in the Graph, the link to the software can be used in the EOSC context.


 ## EOSC Research Software APIs and Connectors (RSAC)

For each mathematical software program, the EOSC Research Software APIs and Connectors (RSAC) will ensure the long-term preservation of research software. We will demonstrate it quickly, as the Software Heritage identifier SWHID of the archived project will be displayed on the new swMATH website.

