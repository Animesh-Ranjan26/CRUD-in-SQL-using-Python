# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:16:25 2024

@author: Animesh Ranjan
"""


"""
Insert into table 
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

insertQuery='''
insert into passenger(name,age,destination) values(%s,%s,%s);

'''
insertValues=[
    ("Raj",23,"Kolkata"),
    ("Neev",12,"Delhi"),
    ("Jack",23,"Mumbai")
]
connection.executemany(insertQuery,insertValues)
database.commit()
database.close()

