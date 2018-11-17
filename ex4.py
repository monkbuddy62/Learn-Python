# these are the total number of cars we have today
cars = 100
# this is the amount of space in the cars
space_in_a_car = 4
# variable telling us how many drivers are availiable today
drivers = 30
# how many passengers need rides today
passengers = 90
# cars that wont be in service today due to lack of drivers
cars_not_driven = cars - drivers
# cars driven really is just the same as drivers, but its less confusing to read if the variable is this
cars_driven = drivers
# how many people we can carpool today
carpool_capacity = cars_driven * space_in_a_car
# the average amount of peeeples per car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars availiable"
print "There are only", drivers, "drivers availiable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
