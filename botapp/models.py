from django.db import models

# Create your models here.

#Users table -- these are indiviuals who will be visiting the site to hire vehicles 
class User(models.Model):
  user_id = models.AutoField(primary_key=True)
  username = models.CharField(max_length=255, unique=True)
  password = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  address = models.TextField()
  phone_number = models.CharField(max_length=20)
  profile_picture = models.ImageField(upload_to='profile_pictures/')
  registration_date = models.DateTimeField(auto_now_add=True)

#car owner table
# In the above code, the CarOwner class represents the model for the Car Owners table.
# Each field in the class corresponds to a column in the table, and you can specify the field types and additional attributes as needed.

class CarOwner(models.Model):
  owner_id = models.AutoField(primary_key=True)
  owner_name = models.CharField(max_length=255)
  OWNER_TYPE_CHOICES = [
    ('Individual', 'Individual'),
    ('Company', 'Company'),
    ]
  owner_type = models.CharField(max_length=10, choices=OWNER_TYPE_CHOICES)
  address = models.TextField()
  phone_number = models.CharField(max_length=20)
  email = models.EmailField(unique=True)
  profile_picture = models.ImageField(upload_to='profile_pictures/')
  registration_date = models.DateTimeField(auto_now_add=True)

##
# The Car model represents the Cars table in the database.
# It includes fields corresponding to the attributes of a car listing, such as car model, year, color, location, availability, rental price, and additional features.
# The 'owner' field establishes a foreign key relationship with the CarOwner model, linking each car to its respective owner.
# The model uses various field types such as CharField, PositiveIntegerField, BooleanField, DecimalField, and TextField to store the car's information.
# The availability field is a boolean indicating whether the car is currently available for booking.
# The rental_price field is a decimal field for storing the rental price of the car.
# The additional_features field is a text field for any additional features or information about the car.
# This model provides the necessary structure for storing and retrieving car listings in the Car Hiring System.


class Car(models.Model):
  car_id = models.AutoField(primary_key=True)
  owner = models.ForeignKey('CarOwner', on_delete=models.CASCADE)
  car_model = models.CharField(max_length=255)
  year = models.PositiveIntegerField()
  color = models.CharField(max_length=50)
  location = models.CharField(max_length=255)
  availability = models.BooleanField(default=True)
  rental_price = models.DecimalField(max_digits=10, decimal_places=2)
  additional_features = models.TextField()

# The Image model represents the Images table in the database.
# It provides a way to store and associate images with specific cars in the Car Hiring System.
# The model includes fields such as image_url, which stores the URL of the image.
# The 'car' field establishes a foreign key relationship with the Car model, linking each image to a specific car.
# The image_url field is an URLField, allowing storage of the image's URL.
# This model enables the system to store and retrieve images associated with car listings, enhancing the visual representation of the cars.

class Image(models.Model):
  image_id = models.AutoField(primary_key=True)
  car = models.ForeignKey('Car', on_delete=models.CASCADE)
  image_url = models.URLField()

# The BookingRequest model represents the Booking Requests table in the database.
# It facilitates the process of customers making requests to book a specific car for a particular date or time period.
# The model includes fields such as car and user, which establish foreign key relationships with the Car and User models, respectively.
# The request_date field stores the date and time when the booking request was made, using the auto_now_add attribute to automatically set the value.
# The request_status field allows tracking the status of the booking request, with choices of 'Pending', 'Accepted', or 'Declined'.
# This model enables the system to manage and track booking requests, providing essential information for car owners to accept or decline reservations.

class BookingRequest(models.Model):
  request_id = models.AutoField(primary_key=True)
  car = models.ForeignKey('Car', on_delete=models.CASCADE)
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  request_date = models.DateTimeField(auto_now_add=True)
  REQUEST_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Declined', 'Declined'),
    ]
  request_status = models.CharField(max_length=10, choices=REQUEST_STATUS_CHOICES)

# The Reservation model represents the Reservations table in the database.
# It handles the confirmed bookings made by customers for specific cars.
# The model includes fields such as car and user, establishing foreign key relationships with the Car and User models, respectively.
# The reservation_date field stores the date and time when the reservation was made, using the auto_now_add attribute to set the value automatically.
# The status field allows tracking the status of the reservation, with choices of 'Confirmed' or 'Cancelled'.
# This model enables the system to manage and track reservations, providing information about the booked cars, users, reservation dates, and status.

class Reservation(models.Model):
  reservation_id = models.AutoField(primary_key=True)
  car = models.ForeignKey('Car', on_delete=models.CASCADE)
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  reservation_date = models.DateTimeField(auto_now_add=True)
  STATUS_CHOICES = [
    ('Confirmed', 'Confirmed'),
    ('Cancelled', 'Cancelled'),
    ]
  status = models.CharField(max_length=10, choices=STATUS_CHOICES)
# The Payment model represents the Payments table in the database.
# It facilitates secure payment processing for rental transactions in the Car Hiring System.
# The model includes fields such as reservation, which establishes a foreign key relationship with the Reservation model.
# The payment_amount field stores the amount of the payment, using the DecimalField for precision.
# The payment_method field stores the chosen payment method for the transaction.
# The payment_date field stores the date and time when the payment was made, using the auto_now_add attribute to automatically set the value.
# This model enables the system to track and record payment information associated with reservations, ensuring secure and reliable payment processing for rental transactions.

class Payment(models.Model):
  payment_id = models.AutoField(primary_key=True)
  reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)
  payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
  payment_method = models.CharField(max_length=50)
  payment_date = models.DateTimeField(auto_now_add=True)
# The Review model represents the Reviews table in the database.
# It allows customers to provide feedback and ratings for the cars and owners they have rented from.
# The model includes fields such as car and user, which establish foreign key relationships with the Car and User models, respectively.
# The rating field stores the numerical rating provided by the customer.
# The review_text field stores the textual feedback or comments.
# The review_date field stores the date and time when the review was submitted, using the auto_now_add attribute to automatically set the value.
# This model enables the system to collect and display reviews and ratings, providing valuable insights for future customers to make informed decisions.

class Review(models.Model):
  review_id = models.AutoField(primary_key=True)
  car = models.ForeignKey('Car', on_delete=models.CASCADE)
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  rating = models.PositiveIntegerField()
  review_text = models.TextField()
  review_date = models.DateTimeField(auto_now_add=True)
# The Notification model represents the Notifications table in the database.
# It facilitates the sending and storage of notifications to users regarding various system events and updates.
# The model includes fields such as user, which establishes a foreign key relationship with the User model.
# The notification_type field stores the type or category of the notification.
# The notification_message field stores the content of the notification.
# The notification_date field stores the date and time when the notification was sent, using the auto_now_add attribute to automatically set the value.
# This model enables the system to send and track notifications to users, providing them with important information about booking requests, confirmations, payment status, and other relevant updates.

class Notification(models.Model):
  notification_id = models.AutoField(primary_key=True)
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  notification_type = models.CharField(max_length=50)
  notification_message = models.TextField()
  notification_date = models.DateTimeField(auto_now_add=True)
# The Admin model represents the Admins table in the database.
# It provides the necessary functionality for managing the overall system and performing administrative tasks.
# The model includes fields such as username, password, email, first name, last name, profile picture, and registration date.
# The password field is typically hashed and salted for secure storage.
# This model allows the system to store and retrieve information about administrators who have access to the admin panel.
# Admin

class Admin(models.Model):
  admin_id = models.AutoField(primary_key=True)
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  profile_picture = models.ImageField(upload_to='admin_profile_pictures/')
  registration_date = models.DateTimeField(auto_now_add=True)
