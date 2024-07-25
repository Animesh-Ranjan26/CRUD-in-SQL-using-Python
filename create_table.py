# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:26:32 2024

@author: Animesh Ranjan
"""

"""
Create table passenger
"""

import mysql.connector
database = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = '12345'
)
connection = database.cursor()
selectdb='use bus_booking'
connection.execute(selectdb)
tableCreationQuery = '''
create table passenger(
    id int primary key auto_increment,
    name varchar(255),
    age int,
    destination varchar(255));
'''
connection.execute(tableCreationQuery)

connection = database.cursor()
describeTableQuery = 'DESC passenger';
connection.execute(describeTableQuery)
for descriptions in connection:
    print(descriptions)
database.close()
connection.execute(printtable)