
## Despite of the new updates in the CodeMeta/Terms   

### i needed to make a search in Schema.org to find some 
### additional properties for the Mapping   


### Documentation for the Mapping   
### Shiraz Malla Mohamad       
### below you can find a table to match each entity from our metadata to the CodeMeta Terms 
 

  | Start Schema          | End Schema           |
|-----------------------|----------------------|
| swMATH                | Codemeta             |
| articles_count        | collectionSize       | 
| authors               | author               |
| classification        | inCodeSet            |  
| dependencies          | softwareRequirements |
| description           | description          |
| homepage              | sameAs               |
| id                    | identifier           |
| keywords              | keywords             |
| license_terms         | license              |
| name                  | name                 |
| operating_systems     | operatingSystem      |
| orms_id               | identifier           |
| programming_languages | programmingLanguage  |
| related_software      | relatedLink          | 
| source_code           | codeRepository       | 
| standard_articles     | Citation             |
| zbmath_url            | url                  |
|                       |                      |

## collectionSize : is used as a subproperty from Schema.org, because we could not find any matching Term in on CodeMeta website.   CollectionSize is The number of items in the Collection   
  you can find it in Schema.org
Thing -> CreativeWork -> Collection 

## inCodeSet : is also a property , which is referring to the categorizing of the scientific classifications , which could be a match for our Mathematical subject classifications.   inCodeSet is a CategoryCodeSet contatins this category code. 
  
## related_software : we mapped it with relatedLink in order to have a solution for it from our zbmath_url/identifier 

## source_code : it is actually the codeRepistory 
  
## one case to be noticed.   
  
  
#### id and orms_id and both of them mtach with identifier property.
#### we have here many to one case.   




  
