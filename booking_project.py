# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:38:50 2024

@author: Animesh Ranjan
"""




"""
Connect mysql with python 
Use database
Create Table
Insert data
Select data
Update data
Delete data
"""

from datetime import datetime
import mysql.connector
database = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = '12345'
)
connection = database.cursor()
selectdb='use bus_booking'
connection.execute(selectdb)

table_create='''
CREATE TABLE booking(
    Passenger_id int primary key auto_increment,
    Passenger_Name varchar(50),
    Passenger_age int,
    num_of_pass int,
    date date,
    price int);
'''
connection.execute(table_create)


available_seat=50
price=1500
while True:
    print("\n1. Seat Availability")
    print("\n2. Booking Portal")
    print("\n3. Show All Bookings")
    print("\n4. Update Booking Details")
    print("\n5. Cancel Booking")
    print("\n6. Exit Application")
    choice = input("\nEnter your choice: ")

    if choice == '1':
        bookingsQuery='''
        SELECT SUM(num_of_pass) FROM booking
        '''
        connection.execute(bookingsQuery)
        bookings = connection.fetchone()
        
        print("available seat is: ", available_seat-bookings[0])

    elif choice == '2':
        Passenger_Name=input("Enter Passenger Name: ")
        Passenger_age=int(input("Enter age of the passenger: "))
        num_of_pass=1
        date = datetime.now().date()
        if Passenger_age>60:
            price=750
        else:
            price=1500
        insertValues = [(Passenger_Name,Passenger_age,num_of_pass,date,price)]        
        insertQuery='''
        Insert into booking(Passenger_Name, Passenger_age, num_of_pass, Date, Price)
        values(%s,%s,%s,%s,%s)
        '''
        connection.executemany(insertQuery,insertValues)
        database.commit()

    elif choice == '3':
        show_all_bookings='''
        SELECT * FROM booking;
        '''
        
        connection.execute(show_all_bookings)
        for rows in connection:
            print(rows)
    
    elif choice == '4':
        Passenger_id = input("Enter Passenger ID to update: ")
        new_name = input("Enter new name: ")
        new_age = int(input("Enter new age: "))
        if new_age>60:
            new_price=750
        else:
            new_price=1500
        update_booking='''UPDATE booking SET Passenger_Name = %s, Passenger_age = %s,price = %s WHERE Passenger_id = %s'''
        connection.execute(update_booking, (new_name, new_age, new_price, Passenger_id))
        print("Booking updated!")
        database.commit()

    elif choice == '5':
        Passenger_id = input("Enter Passenger ID to cancel booking: ")
        cancel_booking='''
        DELETE FROM booking WHERE Passenger_id = %s
        '''
        connection.execute(cancel_booking, (Passenger_id,))
        print("Booking cancelled")
        database.commit()

    elif choice == '6':
        break

else:
    print("Invalid choice! Please try again.")

