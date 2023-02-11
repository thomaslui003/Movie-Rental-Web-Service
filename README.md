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


## Description


### Executing the program

1. Clone the repository on Github
2. Open VsCode with the repository file folder
3. Ensure the Azure SQL server database remain exist for use
3. The application then can be compiled and run in VScode with the success or failure result for each rental interactions by customers displaying on localhost based on the test transaction cases.

