

# declare and initalize variables
cars = 100               # int
space_in_a_car = 4.0    # double
drivers = 30            # int
passengers  = 30        # int

# Delaring and initalizing new variable with other variables
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


# output
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")
