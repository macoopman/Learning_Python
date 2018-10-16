
#this one is like your scripts with argv
def print_two(*arg):
    arg1, arg2 = arg
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that * args is actually pointles, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no arguments

def print_none():
    print("I got nothing'.")


print_two("Johnny", "Bravo")
print_two_again("Johnny", "Bravo")
print_one("First")
print_none()
