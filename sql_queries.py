staging_table_drop = "DROP TABLE IF EXISTS staging"

staging_table= ("""CREATE TABLE IF NOT EXISTS staging (
    FL_YEAR                     BIGINT,  
    FL_QUARTER                  BIGINT,  
    FL_MONTH                    BIGINT,  
    DAY_OF_MONTH             BIGINT,  
    DAY_OF_WEEK              BIGINT,  
    FL_DATE                  VARCHAR, 
    OP_UNIQUE_CARRIER        VARCHAR, 
    OP_CARRIER_AIRLINE_ID    BIGINT,  
    OP_CARRIER               VARCHAR, 
    TAIL_NUM                 VARCHAR, 
    OP_CARRIER_FL_NUM        BIGINT,  
    ORIGIN_AIRPORT_ID        BIGINT,  
    ORIGIN_AIRPORT_SEQ_ID    BIGINT,  
    ORIGIN_CITY_MARKET_ID    BIGINT,  
    ORIGIN                   VARCHAR, 
    ORIGIN_CITY_NAME         VARCHAR, 
    ORIGIN_STATE_ABR         VARCHAR, 
    ORIGIN_STATE_FIPS        BIGINT,  
    ORIGIN_STATE_NM          VARCHAR, 
    ORIGIN_WAC               BIGINT, 
    DEST_AIRPORT_ID          BIGINT,  
    DEST_AIRPORT_SEQ_ID      BIGINT,  
    DEST_CITY_MARKET_ID      BIGINT,  
    DEST                     VARCHAR, 
    DEST_CITY_NAME           VARCHAR, 
    DEST_STATE_ABR           VARCHAR, 
    DEST_STATE_FIPS          BIGINT,  
    DEST_STATE_NM            VARCHAR, 
    DEST_WAC                 BIGINT,  
    CRS_DEP_TIME             BIGINT,  
    DEP_TIME                 FLOAT,
    DEP_DELAY                FLOAT,
    DEP_DELAY_NEW            FLOAT,
    DEP_DEL15                FLOAT,
    DEP_DELAY_GROUP          FLOAT,
    DEP_TIME_BLK             VARCHAR, 
    TAXI_OUT                 FLOAT,
    WHEELS_OFF               FLOAT,
    WHEELS_ON                FLOAT,
    TAXI_IN                  FLOAT,
    CRS_ARR_TIME             BIGINT,  
    ARR_TIME                 FLOAT,
    ARR_DELAY                FLOAT,
    ARR_DELAY_NEW            FLOAT,
    ARR_DEL15                FLOAT,
    ARR_DELAY_GROUP          FLOAT,
    ARR_TIME_BLK             VARCHAR, 
    CANCELLED                FLOAT,
    CANCELLATION_CODE        VARCHAR, 
    DIVERTED                 FLOAT,
    CRS_ELAPSED_TIME         FLOAT,
    ACTUAL_ELAPSED_TIME      FLOAT,
    AIR_TIME                 FLOAT,
    FLIGHTS                  FLOAT,
    DISTANCE                 FLOAT,
    DISTANCE_GROUP           BIGINT,  
    CARRIER_DELAY            FLOAT,
    WEATHER_DELAY            FLOAT,
    NAS_DELAY                FLOAT,
    SECURITY_DELAY           FLOAT,
    LATE_AIRCRAFT_DELAY      FLOAT,
    FIRST_DEP_TIME           FLOAT,
    TOTAL_ADD_GTIME          FLOAT,
    LONGEST_ADD_GTIME        FLOAT,
    DIV_AIRPORT_LANDINGS     BIGINT,  
    DIV_REACHED_DEST         FLOAT,
    DIV_ACTUAL_ELAPSED_TIME  FLOAT,
    DIV_ARR_DELAY            FLOAT,
    DIV_DISTANCE             FLOAT,
    DIV1_AIRPORT             VARCHAR, 
    DIV1_AIRPORT_ID          FLOAT,
    DIV1_AIRPORT_SEQ_ID      FLOAT,
    DIV1_WHEELS_ON           FLOAT,
    DIV1_TOTAL_GTIME         FLOAT,
    DIV1_LONGEST_GTIME       FLOAT,
    DIV1_WHEELS_OFF          FLOAT,
    DIV1_TAIL_NUM            VARCHAR, 
    DIV2_AIRPORT             VARCHAR, 
    DIV2_AIRPORT_ID          FLOAT,
    DIV2_AIRPORT_SEQ_ID      FLOAT,
    DIV2_WHEELS_ON           FLOAT,
    DIV2_TOTAL_GTIME         FLOAT,
    DIV2_LONGEST_GTIME       FLOAT,
    DIV2_WHEELS_OFF          FLOAT,
    DIV2_TAIL_NUM            VARCHAR, 
    DIV3_AIRPORT             VARCHAR,
    DIV3_AIRPORT_ID          FLOAT,
    DIV3_AIRPORT_SEQ_ID      FLOAT,
    DIV3_WHEELS_ON           FLOAT,
    DIV3_TOTAL_GTIME         FLOAT,
    DIV3_LONGEST_GTIME       FLOAT,
    DIV3_WHEELS_OFF          FLOAT,
    DIV3_TAIL_NUM            VARCHAR,
    DIV4_AIRPORT             VARCHAR,
    DIV4_AIRPORT_ID          FLOAT,
    DIV4_AIRPORT_SEQ_ID      FLOAT,
    DIV4_WHEELS_ON           FLOAT,
    DIV4_TOTAL_GTIME         FLOAT,
    DIV4_LONGEST_GTIME       FLOAT,
    DIV4_WHEELS_OFF          FLOAT,
    DIV4_TAIL_NUM            VARCHAR,
    DIV5_AIRPORT             VARCHAR,
    DIV5_AIRPORT_ID          FLOAT,
    DIV5_AIRPORT_SEQ_ID      FLOAT,
    DIV5_WHEELS_ON           FLOAT,
    DIV5_TOTAL_GTIME         FLOAT,
    DIV5_LONGEST_GTIME       FLOAT,
    DIV5_WHEELS_OFF          FLOAT,
    DIV5_TAIL_NUM            FLOAT,
    UNNAMED                  VARCHAR,
    ID_KEY                   VARCHAR NOT NULL PRIMARY KEY)
""")



flight_table_drop = """
DROP TABLE IF  EXISTS flights
"""

airport_table_drop =  """
DROP TABLE IF  EXISTS airports
"""

airline_table_drop =  """
DROP TABLE IF  EXISTS airlines
"""

date_table_drop =  """
DROP TABLE IF  EXISTS dates
"""

dep_perf_table_drop =  """
DROP TABLE IF  EXISTS dep_perfs
"""

arr_perf_table_drop =  """
DROP TABLE IF  EXISTS arr_perfs
"""

summary_table_drop =  """
DROP TABLE IF  EXISTS summaries
"""
gate_info_table_drop =  """
DROP TABLE IF  EXISTS gate_info
"""

diversion_table_drop =  """
DROP TABLE IF  EXISTS diversions
"""



flight_table_create = """
CREATE TABLE IF NOT EXISTS flights (
    ID_KEY VARCHAR NOT NULL PRIMARY KEY,
    FL_DATE                  VARCHAR, 
    OP_UNIQUE_CARRIER        VARCHAR, 
    TAIL_NUM                 VARCHAR, 
    OP_CARRIER_FL_NUM        BIGINT,
    ORIGIN_AIRPORT_ID        BIGINT,  
    DEST_AIRPORT_ID          BIGINT, 
    CANCELLED                FLOAT,
    CANCELLATION_CODE        VARCHAR, 
    DIVERTED                 FLOAT,
    CARRIER_DELAY            FLOAT,
    WEATHER_DELAY            FLOAT,
    NAS_DELAY                FLOAT,
    SECURITY_DELAY           FLOAT,
    LATE_AIRCRAFT_DELAY      FLOAT 
);
"""
airport_table_create =  """
CREATE TABLE IF NOT EXISTS airports (
    AIRPORT_ID        BIGINT NOT NULL PRIMARY KEY,  
    AIRPORT_SEQ_ID    BIGINT,  
    CITY_MARKET_ID    BIGINT,  
    AIRPORT                   VARCHAR, 
    CITY_NAME         VARCHAR, 
    STATE_ABR         VARCHAR, 
    STATE_FIPS        BIGINT,  
    STATE_NM          VARCHAR, 
    WAC               BIGINT 
);
"""

airline_table_create =  """
CREATE TABLE IF NOT EXISTS airlines (
    OP_UNIQUE_CARRIER        VARCHAR NOT NULL PRIMARY KEY, 
    OP_CARRIER_AIRLINE_ID    BIGINT,  
    OP_CARRIER               VARCHAR
);
"""
date_table_create =  """
CREATE TABLE IF NOT EXISTS dates (
    FL_DATE                  VARCHAR NOT NULL PRIMARY KEY, 
    FL_YEAR                     BIGINT,  
    FL_QUARTER                  BIGINT,  
    FL_MONTH                    BIGINT,  
    DAY_OF_MONTH             BIGINT,  
    DAY_OF_WEEK              BIGINT  
);
"""
dep_perf_table_create =  """
CREATE TABLE IF NOT EXISTS dep_perfs(
    ID_KEY VARCHAR NOT NULL PRIMARY KEY,
    CRS_DEP_TIME             BIGINT,  
    DEP_TIME                 FLOAT,
    DEP_DELAY                FLOAT,
    DEP_DELAY_NEW            FLOAT,
    DEP_DEL15                FLOAT,
    DEP_DELAY_GROUP          FLOAT,
    DEP_TIME_BLK             VARCHAR, 
    TAXI_OUT                 FLOAT,
    WHEELS_OFF               FLOAT
);aIR
"""
arr_perf_table_create =  """
CREATE TABLE IF NOT EXISTS arr_perfs (
    ID_KEY VARCHAR NOT NULL PRIMARY KEY,
    WHEELS_ON                FLOAT,
    TAXI_IN                  FLOAT,
    CRS_ARR_TIME             BIGINT,  
    ARR_TIME                 FLOAT,
    ARR_DELAY                FLOAT,
    ARR_DELAY_NEW            FLOAT,
    ARR_DEL15                FLOAT,
    ARR_DELAY_GROUP          FLOAT,
    ARR_TIME_BLK             VARCHAR
);
"""

summary_table_create =  """
CREATE TABLE IF NOT EXISTS summaries (
    ID_KEY VARCHAR NOT NULL PRIMARY KEY,
    CRS_ELAPSED_TIME         FLOAT,
    ACTUAL_ELAPSED_TIME      FLOAT,
    AIR_TIME                 FLOAT,
    FLIGHTS                  FLOAT,
    DISTANCE                 FLOAT,
    DISTANCE_GROUP           BIGINT
);
"""
gate_info_table_create =  """
CREATE TABLE IF NOT EXISTS gate_info (
    ID_KEY VARCHAR NOT NULL PRIMARY KEY,
    FIRST_DEP_TIME           FLOAT,
    TOTAL_ADD_GTIME          FLOAT,
    LONGEST_ADD_GTIME        FLOAT
);
"""
diversion_table_create =  """
CREATE TABLE IF NOT EXISTS diversions (
    ID_KEY VARCHAR NOT NULL PRIMARY KEY,
    DIV_AIRPORT_LANDINGS     BIGINT,  
    DIV_REACHED_DEST         FLOAT,
    DIV_ACTUAL_ELAPSED_TIME  FLOAT,
    DIV_ARR_DELAY            FLOAT,
    DIV_DISTANCE             FLOAT,
    DIV1_AIRPORT             VARCHAR, 
    DIV1_AIRPORT_ID          FLOAT,
    DIV1_AIRPORT_SEQ_ID      FLOAT,
    DIV1_WHEELS_ON           FLOAT,
    DIV1_TOTAL_GTIME         FLOAT,
    DIV1_LONGEST_GTIME       FLOAT,
    DIV1_WHEELS_OFF          FLOAT,
    DIV1_TAIL_NUM            VARCHAR, 
    DIV2_AIRPORT             VARCHAR, 
    DIV2_AIRPORT_ID          FLOAT,
    DIV2_AIRPORT_SEQ_ID      FLOAT,
    DIV2_WHEELS_ON           FLOAT,
    DIV2_TOTAL_GTIME         FLOAT,
    DIV2_LONGEST_GTIME       FLOAT,
    DIV2_WHEELS_OFF          FLOAT,
    DIV2_TAIL_NUM            VARCHAR, 
    DIV3_AIRPORT             VARCHAR,
    DIV3_AIRPORT_ID          FLOAT,
    DIV3_AIRPORT_SEQ_ID      FLOAT,
    DIV3_WHEELS_ON           FLOAT,
    DIV3_TOTAL_GTIME         FLOAT,
    DIV3_LONGEST_GTIME       FLOAT,
    DIV3_WHEELS_OFF          FLOAT,
    DIV3_TAIL_NUM            VARCHAR,
    DIV4_AIRPORT             VARCHAR,
    DIV4_AIRPORT_ID          FLOAT,
    DIV4_AIRPORT_SEQ_ID      FLOAT,
    DIV4_WHEELS_ON           FLOAT,
    DIV4_TOTAL_GTIME         FLOAT,
    DIV4_LONGEST_GTIME       FLOAT,
    DIV4_WHEELS_OFF          FLOAT,
    DIV4_TAIL_NUM            VARCHAR,
    DIV5_AIRPORT             VARCHAR,
    DIV5_AIRPORT_ID          FLOAT,
    DIV5_AIRPORT_SEQ_ID      FLOAT,
    DIV5_WHEELS_ON           FLOAT,
    DIV5_TOTAL_GTIME         FLOAT,
    DIV5_LONGEST_GTIME       FLOAT,
    DIV5_WHEELS_OFF          FLOAT,
    DIV5_TAIL_NUM            FLOAT
);
"""




flight_table_insert = """
INSERT INTO flights (
    ID_KEY  ,
    FL_DATE                  , 
    OP_UNIQUE_CARRIER        , 
    TAIL_NUM                 , 
    OP_CARRIER_FL_NUM        ,
    ORIGIN_AIRPORT_ID        ,  
    DEST_AIRPORT_ID          , 
    CANCELLED                ,
    CANCELLATION_CODE        , 
    DIVERTED                 ,
    CARRIER_DELAY            ,
    WEATHER_DELAY            ,
    NAS_DELAY                ,
    SECURITY_DELAY           ,
    LATE_AIRCRAFT_DELAY
)\
SELECT 
    ID_KEY  ,
    FL_DATE                  , 
    OP_UNIQUE_CARRIER        , 
    TAIL_NUM                 , 
    OP_CARRIER_FL_NUM        ,
    ORIGIN_AIRPORT_ID        ,  
    DEST_AIRPORT_ID          , 
    CANCELLED                ,
    CANCELLATION_CODE        , 
    DIVERTED                 ,
    CARRIER_DELAY            ,
    WEATHER_DELAY            ,
    NAS_DELAY                ,
    SECURITY_DELAY           ,
    LATE_AIRCRAFT_DELAY
FROM staging
ON CONFLICT ON CONSTRAINT flights_pkey
DO NOTHING"""

airport_table_insert_orig = """INSERT INTO airports (    
    AIRPORT_ID        ,  
    AIRPORT_SEQ_ID    ,  
    CITY_MARKET_ID    ,  
    AIRPORT                   , 
    CITY_NAME         , 
    STATE_ABR         , 
    STATE_FIPS        ,  
    STATE_NM          , 
    WAC                
)\
SELECT 
    ORIGIN_AIRPORT_ID        ,  
    ORIGIN_AIRPORT_SEQ_ID    ,  
    ORIGIN_CITY_MARKET_ID    ,  
    ORIGIN                   , 
    ORIGIN_CITY_NAME         , 
    ORIGIN_STATE_ABR         , 
    ORIGIN_STATE_FIPS        ,  
    ORIGIN_STATE_NM          , 
    ORIGIN_WAC                
FROM staging
ON CONFLICT ON CONSTRAINT airports_pkey 
DO NOTHING"""

airport_table_insert_dest = """INSERT INTO airports (    
    AIRPORT_ID        ,  
    AIRPORT_SEQ_ID    ,  
    CITY_MARKET_ID    ,  
    AIRPORT                   , 
    CITY_NAME         , 
    STATE_ABR         , 
    STATE_FIPS        ,  
    STATE_NM          , 
    WAC                
)\
SELECT 
    DEST_AIRPORT_ID        ,  
    DEST_AIRPORT_SEQ_ID    ,  
    DEST_CITY_MARKET_ID    ,  
    DEST                   , 
    DEST_CITY_NAME         , 
    DEST_STATE_ABR         , 
    DEST_STATE_FIPS        ,  
    DEST_STATE_NM          , 
    DEST_WAC                
FROM staging
ON CONFLICT ON CONSTRAINT airports_pkey 
DO NOTHING"""

airline_table_insert = """INSERT INTO airlines (
    OP_UNIQUE_CARRIER        , 
    OP_CARRIER_AIRLINE_ID    ,  
    OP_CARRIER               
)\
SELECT 
    OP_UNIQUE_CARRIER        , 
    OP_CARRIER_AIRLINE_ID    ,  
    OP_CARRIER               
FROM staging
ON CONFLICT ON CONSTRAINT airlines_pkey
DO NOTHING"""


date_table_insert = """INSERT INTO dates (
    FL_DATE                   , 
    FL_YEAR                     ,  
    FL_QUARTER                  ,  
    FL_MONTH                    ,  
    DAY_OF_MONTH             ,  
    DAY_OF_WEEK                
)\
SELECT 
    FL_DATE                   , 
    FL_YEAR                     ,  
    FL_QUARTER                  ,  
    FL_MONTH                    ,  
    DAY_OF_MONTH             ,  
    DAY_OF_WEEK                
FROM staging
ON CONFLICT ON CONSTRAINT dates_pkey
DO NOTHING"""

dep_perf_table_insert = """INSERT INTO dep_perfs (
    ID_KEY  ,
    CRS_DEP_TIME             ,  
    DEP_TIME                 ,
    DEP_DELAY                ,
    DEP_DELAY_NEW            ,
    DEP_DEL15                ,
    DEP_DELAY_GROUP          ,
    DEP_TIME_BLK             , 
    TAXI_OUT                 ,
    WHEELS_OFF               
)\
SELECT 
    ID_KEY  ,
    CRS_DEP_TIME             ,  
    DEP_TIME                 ,
    DEP_DELAY                ,
    DEP_DELAY_NEW            ,
    DEP_DEL15                ,
    DEP_DELAY_GROUP          ,
    DEP_TIME_BLK             , 
    TAXI_OUT                 ,
    WHEELS_OFF               
FROM staging
ON CONFLICT ON CONSTRAINT dep_perfs_pkey
DO NOTHING"""

arr_perf_table_insert = """INSERT INTO arr_perfs (
    ID_KEY  ,
    WHEELS_ON                ,
    TAXI_IN                  ,
    CRS_ARR_TIME             ,  
    ARR_TIME                 ,
    ARR_DELAY                ,
    ARR_DELAY_NEW            ,
    ARR_DEL15                ,
    ARR_DELAY_GROUP          ,
    ARR_TIME_BLK             
)\
SELECT 
    ID_KEY  ,
    WHEELS_ON                ,
    TAXI_IN                  ,
    CRS_ARR_TIME             ,  
    ARR_TIME                 ,
    ARR_DELAY                ,
    ARR_DELAY_NEW            ,
    ARR_DEL15                ,
    ARR_DELAY_GROUP          ,
    ARR_TIME_BLK             
FROM staging
ON CONFLICT ON CONSTRAINT arr_perfs_pkey
DO NOTHING"""

summary_table_insert = """INSERT INTO summaries (
    ID_KEY  ,
    CRS_ELAPSED_TIME         ,
    ACTUAL_ELAPSED_TIME      ,
    AIR_TIME                 ,
    FLIGHTS                  ,
    DISTANCE                 ,
    DISTANCE_GROUP           
)\
SELECT 
    ID_KEY  ,
    CRS_ELAPSED_TIME         ,
    ACTUAL_ELAPSED_TIME      ,
    AIR_TIME                 ,
    FLIGHTS                  ,
    DISTANCE                 ,
    DISTANCE_GROUP           
FROM staging
ON CONFLICT ON CONSTRAINT summaries_pkey
DO NOTHING"""

gate_info_table_insert = """INSERT INTO gate_info (
    ID_KEY  ,
    FIRST_DEP_TIME           ,
    TOTAL_ADD_GTIME          ,
    LONGEST_ADD_GTIME        
)\
SELECT 
    ID_KEY  ,
    FIRST_DEP_TIME           ,
    TOTAL_ADD_GTIME          ,
    LONGEST_ADD_GTIME        
FROM staging
ON CONFLICT ON CONSTRAINT gate_info_pkey
DO NOTHING"""

diversion_table_insert = """INSERT INTO diversions (
    ID_KEY  ,
    DIV_AIRPORT_LANDINGS     ,  
    DIV_REACHED_DEST         ,
    DIV_ACTUAL_ELAPSED_TIME  ,
    DIV_ARR_DELAY            ,
    DIV_DISTANCE             ,
    DIV1_AIRPORT             , 
    DIV1_AIRPORT_ID          ,
    DIV1_AIRPORT_SEQ_ID      ,
    DIV1_WHEELS_ON           ,
    DIV1_TOTAL_GTIME         ,
    DIV1_LONGEST_GTIME       ,
    DIV1_WHEELS_OFF          ,
    DIV1_TAIL_NUM            , 
    DIV2_AIRPORT             , 
    DIV2_AIRPORT_ID          ,
    DIV2_AIRPORT_SEQ_ID      ,
    DIV2_WHEELS_ON           ,
    DIV2_TOTAL_GTIME         ,
    DIV2_LONGEST_GTIME       ,
    DIV2_WHEELS_OFF          ,
    DIV2_TAIL_NUM            , 
    DIV3_AIRPORT             ,
    DIV3_AIRPORT_ID          ,
    DIV3_AIRPORT_SEQ_ID      ,
    DIV3_WHEELS_ON           ,
    DIV3_TOTAL_GTIME         ,
    DIV3_LONGEST_GTIME       ,
    DIV3_WHEELS_OFF          ,
    DIV3_TAIL_NUM            ,
    DIV4_AIRPORT             ,
    DIV4_AIRPORT_ID          ,
    DIV4_AIRPORT_SEQ_ID      ,
    DIV4_WHEELS_ON           ,
    DIV4_TOTAL_GTIME         ,
    DIV4_LONGEST_GTIME       ,
    DIV4_WHEELS_OFF          ,
    DIV4_TAIL_NUM            ,
    DIV5_AIRPORT             ,
    DIV5_AIRPORT_ID          ,
    DIV5_AIRPORT_SEQ_ID      ,
    DIV5_WHEELS_ON           ,
    DIV5_TOTAL_GTIME         ,
    DIV5_LONGEST_GTIME       ,
    DIV5_WHEELS_OFF          ,
    DIV5_TAIL_NUM            
    )\
SELECT
    ID_KEY  ,
    DIV_AIRPORT_LANDINGS     ,  
    DIV_REACHED_DEST         ,
    DIV_ACTUAL_ELAPSED_TIME  ,
    DIV_ARR_DELAY            ,
    DIV_DISTANCE             ,
    DIV1_AIRPORT             , 
    DIV1_AIRPORT_ID          ,
    DIV1_AIRPORT_SEQ_ID      ,
    DIV1_WHEELS_ON           ,
    DIV1_TOTAL_GTIME         ,
    DIV1_LONGEST_GTIME       ,
    DIV1_WHEELS_OFF          ,
    DIV1_TAIL_NUM            , 
    DIV2_AIRPORT             , 
    DIV2_AIRPORT_ID          ,
    DIV2_AIRPORT_SEQ_ID      ,
    DIV2_WHEELS_ON           ,
    DIV2_TOTAL_GTIME         ,
    DIV2_LONGEST_GTIME       ,
    DIV2_WHEELS_OFF          ,
    DIV2_TAIL_NUM            , 
    DIV3_AIRPORT             ,
    DIV3_AIRPORT_ID          ,
    DIV3_AIRPORT_SEQ_ID      ,
    DIV3_WHEELS_ON           ,
    DIV3_TOTAL_GTIME         ,
    DIV3_LONGEST_GTIME       ,
    DIV3_WHEELS_OFF          ,
    DIV3_TAIL_NUM            ,
    DIV4_AIRPORT             ,
    DIV4_AIRPORT_ID          ,
    DIV4_AIRPORT_SEQ_ID      ,
    DIV4_WHEELS_ON           ,
    DIV4_TOTAL_GTIME         ,
    DIV4_LONGEST_GTIME       ,
    DIV4_WHEELS_OFF          ,
    DIV4_TAIL_NUM            ,
    DIV5_AIRPORT             ,
    DIV5_AIRPORT_ID          ,
    DIV5_AIRPORT_SEQ_ID      ,
    DIV5_WHEELS_ON           ,
    DIV5_TOTAL_GTIME         ,
    DIV5_LONGEST_GTIME       ,
    DIV5_WHEELS_OFF          ,
    DIV5_TAIL_NUM            
FROM staging
ON CONFLICT ON CONSTRAINT diversions_pkey
DO NOTHING"""




insert_queries = [flight_table_insert,
airport_table_insert_orig,    
airport_table_insert_dest,    
airline_table_insert,
date_table_insert,
dep_perf_table_insert,
arr_perf_table_insert,
summary_table_insert,
gate_info_table_insert,
diversion_table_insert]


drop_table_queries = [flight_table_drop,
airport_table_drop,
airline_table_drop,
date_table_drop,
dep_perf_table_drop,
arr_perf_table_drop,
summary_table_drop,
gate_info_table_drop,
diversion_table_drop]

create_table_queries = [flight_table_create,
airport_table_create,
airline_table_create,
date_table_create,
dep_perf_table_create,
arr_perf_table_create,
summary_table_create,
gate_info_table_create,
diversion_table_create]