
the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

#same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can o through mixed lists
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build list, first start with an empty one
#elements = []

# then use the range function to do 0 to 5 counts
elements = range(0,100,5)
    # print(f"Adding {i} to the list.")
    # # appending is a function tha lists understands
    # elements.append(i)

#now we can print them out too
for i in elements:
    print(f"Element was: {i}")
