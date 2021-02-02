on the POST/cars: i first get all the cars from the  https://vpic.nhtsa.dot.gov/api/ dataset and only get the one that matches the carmake and carmodel in the body request, once there is a match it saves the car in the database and if no match it returns a not found error.
GET/cars: fetch all the cars in the database
POST/rate/id: you can add a rating to the given car from 1 to 5
GET/popular: fetches the cars according to the id in desc order

Important when entering the urls: dont forget the trailing slash at the end....

POST/cars
GET/cars
POST/popular
POST/rate/id
....
admin panel
username: admin
password: admin

the project is hosted on heroku and the link to live project is:(https://car-api-amir.herokuapp.com/cars/) 

