import pyodbc
from connect_db import connect_db


def loadRentalPlan(filename, conn):
    """
        Input:
            $filename: "RentalPlan.txt"
            $conn: you can get it by calling connect_db()
        Functionality:
            1. Create a table named "RentalPlan" in the "VideoStore" database on Azure
            2. Read data from "RentalPlan.txt" and insert them into "RentalPlan"
               * Columns are separated by '|'
               * You can use executemany() to insert multiple rows in bulk
    """

    conn.execute("CREATE TABLE RentalPlan (pid INT, pname VARCHAR(50), monthly_fee FLOAT, max_movies INT, Primary key (pid))")


    print(pyodbc.drivers())
    print(connect_db())

    with open('RentalPlan.txt') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
     count += 1
     #print(f'line {count}: {line}')
     takeoutSpaces = line.strip()
     lineSplit = takeoutSpaces.split('|')
     conn.execute("INSERT INTO RentalPlan (pid, pname, monthly_fee, max_movies) VALUES (?,?,?,?)", lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3])
    #  print (lineSplit)
    # print ("completed insertion of rentalplan----------------------------")
    


def loadCustomer(filename, conn):
    """
        Input:
            $filename: "Customer.txt"
            $conn: you can get it by calling connect_db()
        Functionality:
            1. Create a table named "Customer" in the "VideoStore" database on Azure
            2. Read data from "Customer.txt" and insert them into "Customer".
               * Columns are separated by '|'
               * You can use executemany() to insert multiple rows in bulk
    """

    conn.execute("CREATE TABLE Customer (cid INT Primary Key, pid INT, username VARCHAR(50), password VARCHAR(50), Foreign key (pid) References RentalPlan (pid) ON DELETE CASCADE)")
    with open('Customer.txt') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
     count += 1
     takeoutSpaces = line.strip()
     lineSplit = takeoutSpaces.split('|')
     conn.execute("INSERT INTO Customer (cid, pid, username, password) VALUES (?,?,?,?)", lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3])
    #  print (lineSplit)
      
    # print ("completed insertion of customer----------------------------")


    

def loadMovie(filename, conn):
    """
        Input:
            $filename: "Movie.txt"
            $conn: you can get it by calling connect_db()
        Functionality:
            1. Create a table named "Movie" in the "VideoStore" database on Azure
            2. Read data from "Movie.txt" and insert them into "Movie".
               * Columns are separated by '|'
               * You can use executemany() to insert multiple rows in bulk
    """
    # WRITE YOUR CODE HERE
    conn.execute("CREATE TABLE Movie(mid INT Primary Key, mname VARCHAR(50), year INT)")
    with open('Movie.txt') as f:
     lines = f.readlines()

    count = 0
    for line in lines:
     count += 1
     takeoutSpaces = line.strip()
     lineSplit = takeoutSpaces.split('|')
     conn.execute("INSERT INTO Movie (mid, mname, year) VALUES (?,?,?)", lineSplit[0], lineSplit[1], lineSplit[2])
    #  print (lineSplit)
      
    # print ("completed insertion of movie----------------------------")



def loadRental(filename, conn):
    """
        Input:
            $filename: "Rental.txt"
            $conn: you can get it by calling connect_db()
        Functionality:
            1. Create a table named "Rental" in the VideoStore database on Azure
            2. Read data from "Rental.txt" and insert them into "Rental".
               * Columns are separated by '|'
               * You can use executemany() to insert multiple rows in bulk
    """

    conn.execute("CREATE TABLE Rental(cid INT, mid INT, date_and_time DATETIME, status VARCHAR(6), Foreign key (cid) References Customer(cid), Foreign key (mid) References Movie(mid) ON DELETE CASCADE)")
    with open('Rental.txt') as f:
     lines = f.readlines()

    count = 0
    for line in lines:
     count += 1
     takeoutSpaces = line.strip()
     lineSplit = takeoutSpaces.split('|')
     if len(lineSplit) == 4:
         conn.execute("INSERT INTO Rental (cid, mid, date_and_time, status) VALUES (?,?,?,?)", lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3])
    
    #  print (lineSplit)
      
    # print ("completed insertion of rental----------------------------")


def dropTables(conn):
    conn.execute("DROP TABLE IF EXISTS Rental")
    conn.execute("DROP TABLE IF EXISTS Customer")
    conn.execute("DROP TABLE IF EXISTS RentalPlan")
    conn.execute("DROP TABLE IF EXISTS Movie")



if __name__ == "__main__":
    conn = connect_db()

    dropTables(conn)

    loadRentalPlan("RentalPlan.txt", conn)
    loadCustomer("Customer.txt", conn)
    loadMovie("Movie.txt", conn)
    loadRental("Rental.txt", conn)


    conn.commit()
    conn.close()






