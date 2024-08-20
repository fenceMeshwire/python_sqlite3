#!/usr/bin/env python3

# Python 3.11

# 03_find_delete_duplicate_rows.py

# Dependency
import sqlite3

dbname = "database_name.db"

con = sqlite3.connect(dbname)
cur = con.cursor()

sql_statement = 'DELETE FROM char_data_types WHERE rowid NOT IN (SELECT min(rowid) FROM table_name GROUP BY col_1, col_2, col_3)'
res = cur.execute(sql_statement)

# a) Test the result with a SELECT statement:
sql_statement = 'SELECT * FROM table_name'
res = cur.execute(sql_statement)
request = res.fetchall() # fetchall()requires a variable to store the data aquired from the database.
for row in request:
    print(row)

# b) Export contents:
import os

sql_statement = 'SELECT * FROM table_name'
res = cur.execute(sql_statement)
request = res.fetchall() # fetchall()requires a variable to store the data aquired from the database.
export_path = r"C:\Users\user\output"
os.chdir(export_path)
with open('csv_export.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['col_1', 'col_2', 'col_3'])
    for row in request:
        writer.writerow(row)
