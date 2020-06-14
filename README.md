# Project Overview

Cassini interview assignment.  

## Introduction

The scope of this repo is twofold 
- Create a DB containing information about flights in 2019
- Use these data to perform a statistical analysis of the delayed departures in San Francisco.

## Dataset
Data are obtained from the [Bureau of Transportation Statistics](https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time). This website allows to download data for a specific year and month, and to select the required information. 

We focus on data from 2019 and download the complete set of info.

Each month corresponds to a .csv file that is stored in the folder ```/data/all``` with a name corresponding to the month. E.g. ```/data/all/5.csv``` corresponds to May 2019.
## Files 
In addition to the data files, there are six files:
1. ```test.ipynb``` displays the first few rows of each table to check the database.
2. ```create_tables.py``` drops and creates the tables. It is used to reset the tables before running the ETL scripts.
3. ```etl.ipynb``` reads and processes a single file from ```song_data``` and ```log_data``` and loads the data into the tables. This notebook contains detailed instructions on the ETL process for each of the tables.
4. ```etl.py``` reads and processes files from ```song_data``` and ```log_data``` and loads them into the tables. It can be filled out based on the ETL notebook.
5. ```sql_queries.py``` contains all the sql queries, and is imported into the last three files above.
6. ```README.md``` this readme.


## Database Schema
The Database schema consists of a star schema, in which however not all of the periferic tables are dimension tables. The database contains the following tables
#### Fact Tables 
1. **flights** 
- - columns:     ID_KEY (PRIMARY KEY),FL_DATE, OP_UNIQUE_CARRIER,TAIL_NUM,OP_CARRIER_FL_NUM,BIGINT,ORIGIN_AIRPORT_ID,BIGINT,DEST_AIRPORT_ID,BIGINT,CANCELLED,FLOAT,CANCELLATION_CODE,VARCHAR,DIVERTED,FLOAT,CARRIER_DELAY,FLOAT,WEATHER_DELAY,FLOAT,NAS_DELAY,FLOAT,SECURITY_DELAY,FLOAT,LATE_AIRCRAFT_DELAY,FLOAT


#### Dimenson Tables
1. **airports** 
- -columns:AIRPORT_ID (PRIMARY KEY),AIRPORT_SEQ_ID,CITY_MARKET_ID,AIRPORT,CITY_NAME, STATE_ABR,STATE_FIPS,STATE_NM,WAC

2. **airlines** 
- -columns: OP_UNIQUE_CARRIER (PRIMARY KEY), OP_CARRIER_AIRLINE_ID,OP_CARRIER               
3. **dates**
- -columns: FL_DATE (PRIMARY KEY),FL_YEAR,FL_QUARTER,FL_MONTH,DAY_OF_MONTH,DAY_OF_WEEK

#### Other 
1. dep_perfs
- -columns: ID_KEY (PRIMARY KEY),CRS_DEP_TIME,DEP_TIME,DEP_DELAY,DEP_DELAY_NEW,DEP_DEL15,DEP_DELAY_GROUP,DEP_TIME_BLK,TAXI_OUT,WHEELS_OFF
2. arr_perfs
- -columns: ID_KEY (PRIMARY KEY),WHEELS_ON,TAXI_IN,CRS_ARR_TIME,ARR_TIME,ARR_DELAY,ARR_DELAY_NEW,ARR_DEL15,ARR_DELAY_GROUP,ARR_TIME_BLK   
3. summaries
- -columns: ID_KEY (PRIMARY KEY),CRS_ELAPSED_TIME,ACTUAL_ELAPSED_TIME,AIR_TIME,FLIGHTS,DISTANCE,DISTANCE_GROUP
4. gate_info
- -columns: ID_KEY (PRIMARY KEY),FIRST_DEP_TIME,TOTAL_ADD_GTIME,LONGEST_ADD_GTIME
5. diversions
- -columns: all the remaining columns in the .csv files

It is organised as a start schema, that simplifies queries about user activities. The Entity Relation Diagram is as follows
![alt text](./fligths_schema.png)

The diagram is generated using [Visual Paradigm](https://online.visual-paradigm.com/diagrams/features/erd-tool/). Primary keys are in bold font. I did not manage to do-undo italics to distinguish numerical entries...


## ETL Pipeline

An identifier key for each flight is created by appending the month to the number of the entry in the ```.csv``` file. E.g. the 42nd flight in May will be uniquely identified by the key ```542```. 

Data are loaded from the ```.csv``` files into a staging table containing all the information. This is done by executing the function ```insert_csv```. These are then divided into each table by executing the function ```fill_star_tables```, which iterates through the queries in the list ```insert_queries```.


## Usage
### Preliminaries
- Execute the section ```Intro``` to create the key identifier and rename the columns to names that are not ambiguous for SQL.
- create the INSERT queries 
### DB creation
- substitute the ```host```, ```dbname```, ```user``` and ```password``` inside the ```create_database``` function. Then run the function to create the DB and get a cursor and a connection to it
### Staging 
- create the staging table by executing ```create_table```
- load data in the staging table. This is done by iterating over the ```.csv``` files in the data folder and executing the function ```insert_csv``` on each of them
### DB filling
- execute ```drop_star_tables``` to drop previously created tables
- execute ```create_star_tables``` to create the tables of the star schema DB
- execute ```fill_star_tables``` to copy the data from the staging tables to the tables of the star schema

### Queries
Example queries for each of the tables can be found in the ```test.ipynb``` file. As additional example, here's a query for checking ...
```
SELECT  s.title, t.weekday 
FROM songplay_table AS sp JOIN song_table AS s ON sp.song_id=s.song_id
                        JOIN time_table AS t ON sp.start_time=t.start_time
```
This should return 
| title         | weekday       |
| ------------- |:-------------:| 
| Setanta matins|2              |
