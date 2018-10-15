from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file ...")
target = open(filename, 'w') #<- make sure to add the 'w' to allow writing, ie. truncating

print("Truncating the file. Goodbye!")
# target.truncate()                     #<- this is redundent. 'w' is what clears everything

print("Now I'm going to ask you for three lines.")
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

# Object maintains its current location while file is open

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# better way to do the above
target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it")
target.close()
