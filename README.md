# Movie-Rental-Web-Service

This repository is to showcase the Movie Rental Web service that allows users to rent movies and keep track of which customers are currently renting what movies.

The video rental store database has the entities characteristics:

RentalPlan(pid INT, pname VARCHAR(50), monthly_fee FLOAT, max_movies INT)\
Customer(cid INT, pidFK-RentalPlan INT, username VARCHAR(50), password VARCHAR(50))\
Rental(cidFK-Customer INT, midFK-Movie INT, date_and_time DATETIME, status VARCHAR(6))\
Movie(mid INT, mname VARCHAR(50), year INT)


RentalPlan: Each plan has a plan id, a name ("Basic", "Rental Plus", "Super Access", or "Ultra Access"), the maximum number of rentals allowed ("Basic" allows one movie, "Rental Plus" allows three, "Super Access" allows five, "Ultra Plus" allows ten), and the monthly fee.

Rental: Each row represents the fact that a movie was rented by a customer with a customer id. The movie is identified by a movie id. The rental has a status that can be "open", or "closed", and the date and time the movie was checked out, to distinguish multiple rentals of the same movie by the same customer. When a customer first rents a movie, then you create an "open" entry in Rentals; when she returns it you update it to "closed" (you never delete it).

### Data loading function onto Azure database
There are four data loading functions that takes in file input and processes the data for Rental Plan, Customer list, Movie list, Rental transaction list, and creates the tables on the Azure SQL server database. 


### HTTP functions for the operation of the movie rental API
* A method to get the renter of a given movie. The renter is represented by cid; the movie is represented by mid. If the movie is not being rented by anyone, return cid = -1.
  * Testing: http://127.0.0.1:5000/getRenterID?mid=1 Response: {'cid': 2}
  * Incorrect case: http://127.0.0.1:5000/getRenterID?mid=4 Response: {'cid': -1}
  
* A method to get how many more movies that a given customer can rent.
  * This HTTP method takes cid as input, and returns n which represents how many more movies that cid can rent.
  * n = 0 means the customer has reached its maximum number of rentals. 
    * Testing: http://127.0.0.1:5000/getRemainingRentals?cid=1 Response: {'remain': 5}
    * http://127.0.0.1:5000/getRemainingRentals?cid=4 Response: {'remain': 1}

* A method that handle the request when a customer wants to rent a movie with the following two constraints always satisfied
  * constraint 1: At any time a movie can be rented to at most one customer.
  * constraint 2: At any time a customer can have at most as many movies rented as his/her plan allows.
  * When a customer requests to rent a movie, the program may deny this request if it violates a constraint via conn.rollback().
  * The HTTP method takes cid and mid as input, and returns either "success" or "fail".
    * Testing: http://127.0.0.1:5000/rent?cid=4&mid=5 Response: {"rent": "success"}
    * http://127.0.0.1:5000/rent?cid=4&mid=6 Response: {"rent": "fail"}
* Another method takes the result of the transaction and use a put method to update the success/failure result with timestamp in the Azure SQL Server database

### Executing the program

1. Clone the repository on Github
2. Open VsCode with the repository file folder
3. Ensure the Azure SQL server database remain exist for use
4. Run the following within the folder directory level in terminal: FLASK_APP=query.py flask
6. The application then can be compiled and run in VScode with the success or failure result for each rental interactions by customers displaying on localhost based on the test transaction cases.

