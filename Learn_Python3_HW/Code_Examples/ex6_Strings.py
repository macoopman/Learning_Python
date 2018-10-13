
# playing with string

# initialize to 10
types_of_people = 10
# using f_string to create an new string
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
# same as above
y = f"Those whoe know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")


#create var hilarious
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
# calling methond on string, format, that inputs into the place holder
# did not create the string as a formatted string.
print(joke_evaluation.format(hilarious))



w = "This is the left side of..."
e = "a string with a right side."
print (w + e)
