    The Mapping of  swmath with codemeta based on the  given codemeta's terms   
    Swmath_article 
  
    Swmath : Code Meta   
    Authors : author  **( Text	The name of an Organization, or if separate given and  family names cannot be resolved for a Person)**
 
      Authors 2 : is same like authors 1 but with small letters   
  

    Title : Citation  **(A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.)** 


    **Source contatins alot of informations which should be analyzed and seperated as   well : its the source of the article** 
    **includes : the year / date , number of pages and the pagination ,  in some cases  the ISBN of the book or a scientific magazine , the name and  place of the    conference which they dicussesd , published or mentioned the software's article as well.**   
    **Source is the most rich column in the swmath_article table**  
        Source : referencePublication **(An academic publication related to the    software.)**
       source : citation 
       source : datePublished 
       Source : applicationSubCategory	**(Subcategory of the application, e.g. ‘Arcade Game’.)**

     Year : datePublished


    Remarks : applicationCategory   **(Type of software application, e.g. ‘Game, Multimedia’.)**

    last_modified : dateModified **(The date on which the CreativeWork was most recently modified or when the item’s entry was modified within a DataFeed.)**

    pagination :  Position  (describes where and how many pages took the article's software in the source of publication . )  and (The position of an item in a series or sequence of items. (While schema.org considers this a property of CreativeWork, it is also the way to indicate ordering in any list (e.g. the Authors list). By default arrays are unordered in JSON-LD)

    n_zitiert : it might be in important column , zitiert : citation or cited i think perhaps this coulmn refers to how many times this software where mentioned in the scientific articles 



    swmath_software.   
     name : name **The name of the item (software, Organization)**

    Homepage : url **(URL of the item.)**
    Homepage : relatedLink **(A link related to this object, e.g. related web pages)**
    Homepage : sameAs **(	URL of a reference Web page that unambiguously indicates the item’s identity. E.g. the URL of the item’s Wikipedia page, Wikidata entry, or official website.)**

    **there are  many options that could suit the homepage column i added them all to let you choose one of them .** 

    homepage is a very important column in our metadata 
 
     description : description	**(A description of the item.)**
     description : we have 11 items (softwares) that does not have descriptions 

    keywords : keywords **(Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.)**

    authors : author **(The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.)**

    authors : creator **(The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork.)** 

    **Authors : this column has ca 627 - 640 rows that ar empty or has null value** 
  
         i am using this query to make the conclusion about the empty rows 
  
            SELECT COUNT(*) AS empty_row_count
            FROM swmath_software
            WHERE authors IS NULL OR authors = '';
            
       areas_of_application : applicationCategory **(Type of software application, e.g. ‘Game, Multimedia’ ect...)**

     **areas_of_application : i have to mention that this column is almost empty : 42279 rows are empty or have null values** 

    current_version : softwareVersion (Version of the software instance.)
    **it has 42397 empty or null value rows** 


    within this query we could have the number of the filled rows 
      SELECT current_version
      FROM swmath_software
      WHERE current_version IS not NULL;
      
    **we have only 525 rows in this column and they contain several kind of informations such like : the software's version , in some of them they have i guess the release date of the mentioned  version , some rows has the word none** 

    liecence_terms : license **(A license document that applies to this content, typically indicated by URL.)**

     SELECT COUNT(*) AS Result
     FROM swmath_software
     WHERE licence_terms IS not  NULL;
     
    only 931 rows are filled with informations 
    but even those rows can not provide us with rich informations 
    
    many of them has the words (none , free)
    the most repeated types of licence are GNU . cpc . GPL , commercial   and and less are Artistic , BSD , Freeware , licence-terms 
    with this query we can get empty rows 
    
    SELECT COUNT(*) AS Result
    FROM swmath_software
    WHERE licence_terms IS NULL OR licence_terms = '';
    **this is the number of the empty rows in this column** 
    **41988** 
    
    
    SELECT COUNT(*) AS Result
    FROM swmath_software
    WHERE licence_terms IS not  NULL;
    we have only 931 with filled informations about the programming lanugaes of the softwares 
    
    
    
       Programming_languages : programmingLanguage **(The computer programming language.)**
    
    
       this column is also almost empty 
       the count of  empty rows is 42389 
    
       
    
         SELECT COUNT(*) AS Result
         FROM swmath_software
          WHERE programming_languages IS NULL OR programming_languages = '';
         this number is for the empty rows in this column 41738
         
          Operating_systems : operatingSystem **(Operating systems supported (Windows 7, OSX 10.6, Android 1.6).)**
    
    
          this column is also almost empty 
          the count of  empty rows is 42389 
    
          only 529 are provided with informations about the operating systems 
      
      
         Interfaces : runtimePlatform **(Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3, .Net Framework 3.0). Supersedes runtime.)**
      
      
      
         its almost an empty column which hast 42377 empty or null valued rows.   
  
         only 541 rows does contatin some informations about programms and programming languages for this softwares 


         Granularity : targetProduct (Target Operating System / Product to which the code applies. If applies to several versions, just the product name can be used.)
   
         it contatins the informations about the libraries of the programming lanugages if exists 
   
         it contains only 262 rows with informations   
         like none , grnularity , stand-alone , open gl toolbox or libraries 
   
   
        42656 are empty rows or null valued 
   
   
   
   
          Dependencies :  softwareRequirements**(Required software dependencies)**
          
   
        
   
   
         here we have 16804 are filled with the informations about the dependencies of these softwares : such like R , Matlab , Fortran etc...   
  

   
         we still have in dependencies  26133 empty or null valued rows 
   
   
         remarks :  is actually ambigous for me . i dont know how could i classify it   
  
  
  
        Source : citation (A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.) contatins only few filled rows   
        with repeated source or websites   
        http://dl.acm.org/  **ACM Digital library : is a community engaged with  a repository of resources computing research and practice**  , 
         the access to this provided source is forbidden http://cpc.cs.qub.ac.uk/summaries/ 


      The source has websites and the ACM ORG : contatins articles that are mentioning the softwares in out DB 

      orms_id :   (	Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3, .Net Framework 3.0). Supersedes runtime.)     

      only 92 rows are filled with their id numbers , otherwise its almost empty 
      SELECT orms_id
    
     FROM swmath_software
     WHERE orms_id  != '';
     
     and this query shows us the null or empty rows 
     
     SELECT count(*) AS Result from swmath_software
     WHERE orms_id is null or orms_id = '';
     
     the result is : 42826 rows 
     
     

    www_link : citation (A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.) 
    
     this column contain the web links of the publications from the softwares 
     and some of them are referring to the bibliography 


    has 41758 null values  or empty rows 


    we only have 1160 rows that are provided with the links   
    we can review them by writing this sql query   
    SELECT www_link FROM swmath_software
    WHERE www_link  != '';
    
    
    and this query shows us the count of the filled rows 
    SELECT count(*) AS Result from swmath_software
    WHERE www_link  != '';
    
    
    authors2 : author (The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably)
    
    the authors column as richer than authors2 
    authors 2 have the repeated names from the authors column 
    
    its also almost empty 
    
    this query shows us the number of empty or null valued rows 
    36623
    
    SELECT count(*) AS Result from swmath_software
    WHERE authors2 is null or authors2 = '';
    
    if we want to compare the both columns 
    the column authors is richer than the 2nd one 
    
    au_links : is totally empty 
    
    
    similar_sw1 : softwareSuggestions (Optional dependencies , e.g. for optional features, code development, etc)
    
    i have to ask moritz and maxence about it 
    
    is full of informations 
    only 2527 are null valued or empty 
    
    similar_Sw2 : is fully empty column or have null values   
    i tried to query but did not get any good results 
    
    select count(*)AS Result  from swmath_software
    where swmath_software.similar_sw2 is  null or similar_sw2  = '';
    
    result is : 42918 empty , null columns 
    
    
    Last_modified : dateModified (The date on which the CreativeWork was most recently modified or when the item’s entry was modified within a DataFeed.)
    
    the date is 09.06.2023 
    
    refman :  provider (The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller. Supersedes carrier.) 
    
    is acutually an important column but unfortuantely it is empty 
    only few columns are provided with links that lead to the packages , tutorials 
    
    42913 the number of empty or null valued rows 
    select count(*)AS Result  from swmath_software
    where swmath_software.refman is  null or refman  = '';
    
    class4filter : fileFormat (Media type, typically MIME format (see IANA site) of the content e.g. application/zip of a SoftwareApplication binary. In cases where a CreativeWork has several media type representations, ‘encoding’ can be used to indicate each MediaObject alongside particular fileFormat information. Unregistered or niche file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia entry.)
    arxiv : is for the mathematical softwares for example 
    it determine the type of the data in the xml body according to DATAcite 
    
    
    could be an important column but 42910 are empty rows or null valued 
    
    
    peerjour : citation 
    
    the only filled column refers to the mpc : Mathematical Programming Computation (MPC) publishes original research articles advancing the state of the art of practical computation in Mathematical Optimization and closely related fields
    <a target="_blank" href="http://mpc.zib.de/MPC/information/authors.html">MPC</a>
    
    
    
    select count(*)AS Result  from swmath_software
    where swmath_software.peerjour is  null or peerjour = '';
    
     are empty rows or null valued  42917
     
     
     keyw_csv : keywords(Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.)  

     
     
     
      select count(*)AS Result  from swmath_software
      where swmath_software.keyw_csv is  null or keyw_csv = '';

     
     29594 are empty or null valued 
     
     SELECT  count(*)  AS Result from swmath_software
     WHERE swmath_software.keyw_csv is not null or swmath_software.keyw_csv != '';
     15729 have values contatin keywords 
     
     msc3 , msc2 , msc5 : are totally ambigous for me 
     n_msc is realted to the three above mentioned columns
     
     msc_descr : has html body but i dont know what refers to 
     
     
     hp_archive : sameAs(	URL of a reference Web page that unambiguously indicates the item’s identity. E.g. the URL of the item’s Wikipedia page, Wikidata entry, or official website.)
     
     
     select count(*)AS Result  from swmath_software
     where swmath_software.hp_archive is  null or hp_archive = '';
     42723 are empty or null valued rows 
     
     only 231 are provided with urls and many of them are broken (not accessable)
     
     
     soi : all rows are empty or null valued 
     svoi also is empty 
     
     
     Github : codeRepository (	Link to the repository where the un-compiled, human readable code and related code is located (SVN, GitHub, CodePlex, institutional GitLab instance, etc.)
     
     unfortuantely not all of rows are provided with the repository of the softwares   
     27587 are empty or null valued 
     
     15349 are provided with their repositories 
     
     search_vector : i have to ask about it 
     
     authors_tsv : empty or null valued 
     
     name_tsv and description_tsv , keywords_tsv , classification , programming_languages_tsv , and the rest of columns with the ending of TSV are empty or null valued 
     42900
     
     
     swmath_software_articles 
     
     software_id : all of rows are filled 
     
     
     rank_msc : 547847 rows are empty or lets say with 0 value 
     and 13928 has other values 
     
     
     article_id : none of the rows is empty and all of them have values