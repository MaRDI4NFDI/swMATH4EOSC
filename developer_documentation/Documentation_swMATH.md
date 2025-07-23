# Software Metadata Documentation
This documentation describes the swMATH endpoint of the REST API service supported by zbMATH Open:
[https://api.zbmath.org/v1/software/](https://api.zbmath.org/v1/software/)

## Core Metadata Fields

### Identification
- **`<id>`**  
  Unique identifier for the software (e.g., `oai:swmath.org:3370`).  
  *Format*: OAI-PMH or system-specific URI.

- **`<name>`**  
  Software name (e.g., `MCDA`).  

- **`<description>`**  
  Brief description of the software (e.g., licensing or functionality notes).  

### Attribution
- **`<authors>`** (Repeatable)  
  List of authors/contributors (e.g., `Meyer, Patrick`, `Bigaret, Sébastien`).  

### Technical Context
- **`<dependencies>`**  
  Required dependencies (e.g., `R`).  

- **`<programming_languages>`**  
  *Empty in sample*; would list languages used (e.g., Python, Java).  

- **`<operating_systems>`**  
  *Empty in sample*; would list compatible OS (e.g., Windows, Linux).  

### Classification & Topics
- **`<classification>`** (Repeatable)  
  Numeric codes for subject areas (e.g., `90`, `91` for mathematics).  

- **`<keywords>`**  
  *Empty in sample*; would list thematic keywords.  

### References
- **`<references>`** (Repeatable)  
  Publication IDs (e.g., `7428106`, `7540838`).  

- **`<references_alt>`** (Repeatable)  
  Alternate reference formats (e.g., `7428106;10.1007/978-981-33-4745-8`).  

- **`<references_year_alt>`** (Repeatable)  
  Years of publication (e.g., `2021`, `2022`).  

### Relations
- **`<related_software>`** (Repeatable)  
  Nested entries with:  
  - `<id>`: Unique identifier (e.g., `11029`).  
  - `<name>`: Software name (e.g., `diviz`, `D-Sight`).  

### Licensing & Access
- **`<license_terms>`**  
  *Empty in sample*; would describe usage rights.  

- **`<homepage>`**  
  Official URL (e.g., CRAN page for R packages).  

- **`<source_code>`**  
  Code repository link (e.g., GitHub).  

### Metrics
- **`<articles_count>`**  
  Number of associated publications (e.g., `2`).  

- **`<source_year>`**  
  Release year (e.g., `2022`).  

## Notes
- **Repeatable fields**: Multiple values may appear as siblings (e.g., `<authors>`, `<classification>`).  
- **Empty fields**: Some are placeholders (e.g., `<keywords>`) for optional data.  
- **Nested structures**: `<related_software>` contains child elements.  

---
