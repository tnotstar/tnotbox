# assigns 100 to cars
cars = 100
# sets 4.0 to space_in_a_car
space_in_a_car = 4.0
# sets 30 to drivers
drivers = 30
# sets 90 to passengers
passengers = 90
# evaluates cars - drivers and assigns it to cars_not_driven
cars_not_driven = cars - drivers
# sets drivers to cars_driven
cars_driven = drivers
# calculates carpool_capacity as cars_driven multiplied by space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# calculates average_passengers_per_car as passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")