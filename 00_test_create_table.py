#!/usr/bin/env python3

# Python 3.9.5

# 00_test_create_table.py

# Purpose: Test if a table with a specific name exists in your SQLite3 database.

# Dependencies:
import os, platform
from pathlib import Path
import sqlite3

# Set your working directory (not necessarily needed):
class Cwd():
    def __init__(self):
        self.posix = ''     # Enter the current working directory here (OS X)
        self.windows = ''   # Enter the current working directory here (Windows)

    def setWorkingDirectory(self):
        if os.name == 'posix' or platform.system() == 'Darwin': 
            os.chdir(self.posix)
        elif os.name == 'nt' or platform.system() == 'Windows': 
            os.chdir(self.windows) # Change current working directory.
        os.chdir(self.windows) # Change current working directory.
        return Path.cwd() # Check working directory.

oCwd = Cwd()
oCwd.setWorkingDirectory()

# =================================================================================================
# Core function is to check if a database including one specific table exists, otherwise to create:
# 1.) the database: 'your_database.db'  and
# 2.) the table:    'tbl_Data'          with 
# 3.) the schema:   'tbl_Data(number INTEGER PRIMARY KEY, filename TEXT, filesize INTEGER)'
# 
# If the database already exists, return the number of the last record, otherwise return 0. 

def try_table():
    try:
        database = 'your_database.db'
        table = 'tbl_Data'
        # Create a connection to the database 
        connection = sqlite3.connect(database)
        # Create a database cursor
        cursor = connection.cursor()
        # Create a table
        sql = "CREATE TABLE {}(number INTEGER PRIMARY KEY, filename TEXT, filesize INTEGER)".format(table)
        cursor.execute(sql)
        connection.close()
        print('Table {} created successfully in database: {}'.format(table, database))
    except sqlite3.OperationalError as err:
        print('Error:', err)
  
def get_last_record():
    database = 'your_database.db'
    table = 'tbl_Data'
    try:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        sql = 'SELECT * FROM {};'.format(table)
        cursor.execute(sql)
        records = []
        counter = 0
        algorithm = ''
        try:
            for record in cursor:
                records.append(record)
                counter += 1
            number, filename, filesize = records[counter-1]
        except IndexError:
            print('First records in the table!')
            number = 0
        connection.commit()
        connection.close()
    except sqlite3.OperationalError as err:
        print('Error:', err)
    return number

if __name__ == '__main__':
    try_table()
    last_record = get_last_record()
    print(last_record)
