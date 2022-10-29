#!/usr/bin/env python3

# Python 3.9.5

# Purpose: Create a table in the local sqlite3 database 'database.db'

# Dependencies
import sqlite3
import os

path = 'C:\\Users\\user\\...' # Set current working directory
os.chdir(path)

# Data - important for table layout:
order = [
    {'cat': 1, 'art': 'beer', 'ppu': 4.2, 'cpu': 4.2, 'qty': 1},
    {'cat': 1, 'art': 'water', 'ppu': 1.8, 'cpu': 1.8, 'qty': 1},
    {'cat': 1, 'art': 'water big', 'ppu': 3.0, 'cpu': 3.0, 'qty': 1},
    {'cat': 1, 'art': 'juice', 'ppu': 3.9, 'cpu': 3.9, 'qty': 1},
    {'cat': 1, 'art': 'main dish 1', 'ppu': 13.5, 'cpu': 13.5, 'qty': 1},
    {'cat': 1, 'art': 'main dish 2', 'ppu': 15.5, 'cpu': 15.5, 'qty': 1}
    ]

# Transform data for input: Prop down integrated dictionaries to lists:
simplified_order = []
for item in order:
    position = []
    position = [value for key, value in item.items()]
    simplified_order.append(position)

# Connect to or create the database "restaurant.db"
database = sqlite3.connect('restaurant.db')
csr = database.cursor()

# Create a table which is suitable for the data above:
# Schema: cat|art|ppu|cpu|qty
csr.execute('CREATE TABLE customer_orders (cat integer, art text, ppu real, cpu real, qty integer)')

# Commit the data (simplified_order) to the database:
csr.executemany('insert into customer_orders values (?,?,?,?,?)', simplified_order)
database.commit()
