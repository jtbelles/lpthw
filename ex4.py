# LPTHW ex4.py

# A variable for the number of cars
cars = 100

# A variable for how much space is available in each car
space_in_a_car = 4.0

# Number of available drivers
drivers = 30

# Number of available passangers
passengers = 90

# Determining the number of cars that will not be driven
cars_not_driven = cars - drivers

# Variable to show the number of cars driven
# a bit redundent given the 'drivers' variable
cars_driven = drivers

# Determining the carpool capacity
carpool_capacity = cars_driven * space_in_a_car

# Determining the number of passangers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
