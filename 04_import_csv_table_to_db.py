#!/usr/bin/env python3

# Python 3.11

# 04_import_csv_table_to_db.py

# Database creation and data population.

# Dependencies
import os
import sqlite3
import pandas as pd # This is important, since pandas allows for sql import directly, using the existing connection.

path = r"C:\sqlite3_dir"
os.chdir(path)

dbname = "test_db.db"
con = sqlite3.connect(dbname)
cur = con.cursor()

# Create table:
sql_statement = """
CREATE TABLE us_counties_pop (
    state_fips text,                         
    county_fips text,                        
    region smallint,                        
    state_name text,                         
    county_name text,                        
    area_land bigint,                        
    area_water bigint,                       
    internal_point_lat numeric(10,7),        
    internal_point_lon numeric(10,7),        
    pop_est integer,                    
    pop_est integer,                    
    births integer,                     
    deaths integer,                     
    international_migr integer,         
    domestic_migr integer,              
    residual integer,                   
    CONSTRAINT counties_key PRIMARY KEY (state_fips, county_fips)	
)
"""
cur.execute(sql_statement)

# Import data from csv-file:
import_dir = r"C:\Users\user\input_dir"
os.chdir(import_dir)

df = pd.read_csv('input_dir.csv')
df.to_sql('us_counties_pop_est', con, if_exists='append', index=False)

# Check input data
sql_statement = 'SELECT * FROM us_counties_pop_est_2019'
res = cur.execute(sql_statement)
request = res.fetchall() # fetchall()requires a variable to store the data aquired from the database.
i = 0
for row in request:
    i += 1
print(i) # Check row number against rows in CSV file.
