#!/usr/bin/env python3

# Python 3.9.5

# Purpose: Test if a table with a specific name exists in your SQLite3 database.

# Dependencies:
import os, platform
from pathlib import Path
import sqlite3

# Set your working directory:
class Cwd():
    def __init__(self):
        self.posix = ''
        self.windows = ''

    def setWorkingDirectory(self):
        if os.name == 'posix' or platform.system() == 'Darwin': 
            os.chdir(self.posix)
        elif os.name == 'nt' or platform.system() == 'Windows': 
            os.chdir(self.windows) # Change current working directory.
        os.chdir(self.windows) # Change current working directory.
        return Path.cwd() # Check working directory.

oCwd = Cwd()
oCwd.setWorkingDirectory()

def tryTable():
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
        
tryTable()
