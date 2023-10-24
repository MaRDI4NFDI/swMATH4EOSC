# swMATH and FairCore4Eosc

A reminder of  the FAIR definition: https://en.wikipedia.org/wiki/FAIR_data

FAIRCORE4EOSC is the project of the European Open Science Cloud (EOSC) to develop FAIR components in the EOSC.

The European Open Science Cloud (EOSC) is an ecosystem of research data and related services that will enable and enhance seamless access to and reliable re-use of FAIR research outputs such as data, publications, software, and more.

One of the priorities highlighted in the EOSC Strategic Research and Innovation Agenda (SRIA) is the establishment of the Web of FAIR data and a Minimum Viable EOSC by 2027, featuring the core components and functions to enable EOSC to operate. The development of the EOSC-Core was initiated in the Horizon 2020 calls, which have delivered a rich palette of use cases, demonstrations, data, services, and tools. However, there are still challenges that require to be addressed.
# WP7 The Mathematics Case Study

The FIZ Karlsruhe will demonstrate the usefulness of the core components for mathematicians.

Here we list the adopted components for the mathematics case study of the Work Package 7: 


 ## EOSC Research Software APIs and Connectors (RSAC)

Software Heritage is the world library for source code. As a pillar of the RSAC component, swMATH and SWH will collaborate to preserve mathematical software artifacts.
For each mathematical software program, the RSAC will ensure the long-term preservation of research software source code and metadata. For every open-source software:
* The software will be archived, and a URL link will be displayed on the new swMATH website.
* The user will find the Software Heritage identifier (SWHID) of the source code related to the software artifact on the swMATH website
* The swMATH metadata will be findable on Software Heritage
* The swMATH metadata will be downloadable in CodeMeta and DataCite format

 ## EOSC PID Meta Resolver (PIDMR).
The PIDMR will assist users in controlling for a set of defined PIDs (DOI,SWHID, etc.) that the PID is unique and reliable.
Though, we will show how a mathematician can control the information of PID coming from swMATH in the EOSC PID Meta Resolver (PIDMR)

##  EOSC Metadata Schema and Crosswalk Registry (MSCR)

The  EOSC Metadata Schema and Crosswalk Registry (MSCR) aims to support the publishing, discovery, and access of metadata schemata and provides functions to operationalize metadata conversions by combining crosswalks. Through the new API, research software programs and their metadata will be easily accessible, in particular via the CodeMeta standard. This component will be exposed so that one can use it to convert metadata of mathematical research software to ease the querying process.

What is the schema, and what is the crosswalk?

schema: CodeMeta
crosswalk: mapping from swMATH internal data model to CodeMeta (link to GitHub issue)

To do: add the swMATH mapping between swMATH and CodeMeta to the crosswalk registry.



##  EOSC Data Type Registry (DTR) 

The Data Type Registry is a component allowing for registering the properties of any digital object, such as it can help with the interoperability between services when it comes to sharing resources together.
The FIZ Karlsruhe whiches to use the service for two use cases:
* Mathematics Subject Classification (MSC https://zbmath.org/classification/) should be added as a domain-specific data type to DTR
* Mathematics, particularly LaTeX source code in titles as a domain-specific special case of the horizontal title field. Examples https://zbmath.org/1497.14042 and https://arxiv.org/abs/2004.08860 https://www.sciencedirect.com/science/article/abs/pii/S0021869321003021?via%3Dihub https://zbmath.org/7707391 https://zbmath.org/7658943 https://zbmath.org/7594811. Possible general alternatives are Title as HTML, Title as Image,
* What is currently in DTR that should be adopted by swMATH or zbMATH Open


 ## EOSC Persistent Identifier Graph (PIdGraph)

Moreover, swMATH will integrate into the EOSC PIDGraph, which improves the way of interlinking research entities across domains and data sources based on PIDs (Persistent Identifiers); this can play a crucial role in helping applied mathematicians to identify the most convenient mathematical research software programs.


## EOSC Research Discovery Graph (RDGraph)
Eventually, links between software and publications will also be discoverable via the EOSC Research Discovery Graph (RDGraph), which ensures that whenever a paper associated with a software that is indexed in swMATH is found in the Graph, the link to the software can be used in the EOSC context.


##  Research Activity Identifier (RAiD) 
Research projects in Mathematics that are identified with a Research Activity Identifier (RAiD) should be harvestable through the PIDGraph API. These RAiDs must be linked with other PIDs like ORCID and DOIs.
