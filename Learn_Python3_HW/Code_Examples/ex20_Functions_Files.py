# This imports the argv from the system library
from sys import argv

# variables that hold the user input from argv
script, input_file = argv


# Function takes a file object as a paramerter and call
# the read function inorder to print the whole file
# passed by "REFERENCE" 
def print_all(f):
    print(f.read())


# Function takes a file object as a variable and resets it to the 0th bit.
# ie the beginning
def rewind(f):
    f.seek(0)


# takes and integer input for display only and a file object
# calls readline on the file
# NOTE: file object is tracking what line has been read and each call increments that
def print_a_line(line_count, f):
    print(line_count,":", f.readline())



# open the file give to argv and store the file object in a variable
current_file = open(input_file)

print("First let's print the whole file: \n")

# call print_all fuction onthe object
print_all(current_file)


print("Now lets rewind, kind of like a tape")
rewind(current_file)


print("Let's print three lines:")


# no ++ in python
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
