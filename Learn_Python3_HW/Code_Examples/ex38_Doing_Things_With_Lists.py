
# create string
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Lets fix that.")

#seperate string items at the space and put each word in the list
stuff = ten_things.split(' ')

# list of items to be added to stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# loop while the stuff list is less than 10
while len(stuff) != 10:
    # remove and store the last element of more_stuff
    next_one = more_stuff.pop()
    print("Adding: ", next_one)

    # add that removed element to the end of stuff
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Lets do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print('   '.join(stuff))
print('#'.join(stuff[3:5]))
