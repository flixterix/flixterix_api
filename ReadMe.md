# Flixterix API 

## Technologies 
* Django REST API framework  
* Python 
* PostgreSQL 


## Data Model 
* There are three types of objects in the Flixterix database: movies, dates, and genres. 
* Below is the data model for the database. 

| **Dates**               | **Genres**      |**Movies - Genres (association table)**| **Movies**          | 
|:-----------------------:|:--------------: |:-------------------------------------:|:-------------------:|       
| release_year* <int>     | genre_id* <int> |movie_id* <int>                        | movie_id* <int>     |
| movie_ids** <list>      | name** <str>    |genre_id** <int>                       | release_year** <int>|
|                         |                 |                                       | title <str>         |


Properties with one asterisk (*) are primary keys.  
Properties with two asterisks (**) are foreign keys. 

