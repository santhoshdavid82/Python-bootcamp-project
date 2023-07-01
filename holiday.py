# DS T14 Compulsory Task 1 - Beginner Programming with Functions — Defining Your Own Functions

# Calculate a user’s holiday cost including the plane cost, hotel cost, and car rental cost.

# In this code, we have defined four functions: hotel_cost, plane_cost, car_rental, and holiday_cost.

# The hotel_cost function takes the number of nights as an argument and returns the total cost of the hotel stay.
def hotel_cost(num_nights):
    # Assuming a hotel cost of £100 per night.
    return num_nights * 100

# The plane_cost function takes the city of flight as an argument and returns the cost of the flight based on the chosen city.
def plane_cost(city_flight):
    if city_flight == "Dubai":
        return 500
    elif city_flight == "New York":
        return 800
    elif city_flight == "Tokyo":
        return 1000
    else:
        return 0
    
# The car_rental function takes the number of rental days as an argument and returns the total cost of the car rental. 
def car_rental(rental_days):
    # Assuming a daily rental cost of £50.
    return rental_days * 50

# The holiday_cost function takes the three arguments mentioned and 
# calculates the total cost of the holiday by calling the other functions.
def holiday_cost(num_nights, city_flight, rental_days):
    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days)

    return total_hotel_cost + total_plane_cost + total_car_rental_cost

# Ask the user for inputs.
city_flight = input("Please enter the city you will be flying to (Dubai/New York/Tokyo): ")
num_nights = int(input("Please enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Please enter the number of days you will be hiring a car for: "))

total_cost = holiday_cost(num_nights, city_flight, rental_days) # Calculate the total holiday cost.

# Print out the holiday details.
print("Holiday Details:")
print(f"City of Flight: {city_flight}")
print(f"Hotel Cost: £{hotel_cost(num_nights)}")
print(f"Flight Cost: £{plane_cost(city_flight)}")
print(f"Car Rental Cost: £{car_rental(rental_days)}")
print(f"Total Holiday Cost: £{total_cost}")
