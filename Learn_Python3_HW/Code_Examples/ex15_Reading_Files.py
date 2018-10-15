
from sys import argv

script, filename = argv

#getting the file and storing in in txt
#open creates a file OBJECT, below we call a function on it
txt = open(filename)

print(f"\nHere's your file {filename}\n")
#reading the file and printing it to the screen
print(txt.read())

txt.close()

# print("Type the file name again: ")
# file_again = input("> ")
#
# txt_again = open(filename)
#
# print(txt_again.read())
