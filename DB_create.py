# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:38:32 2024

@author: Animesh Ranjan
"""

""" 
Connect mysql with python 
Create database
"""

import mysql.connector
database = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = '12345'
)

connection = database.cursor()
databaseCreationQuery = 'CREATE DATABASE bus_booking'
connection.execute(databaseCreationQuery)
displayingDatabaseQuery = 'SHOW DATABASES'
connection.execute(displayingDatabaseQuery)
for databases in connection:
    print(databases)
connection=database.cursor()
database.close()
