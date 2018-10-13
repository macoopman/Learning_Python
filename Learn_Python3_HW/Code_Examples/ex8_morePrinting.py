

# creates a formatter object with 4 place holder
# we did something similar in ex7 except we called .format directly on the string, not a string variable
formatter = "{} {} {} {}"


#filling the placeholders of the formatter object
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format("Try your", "Own test here", "Maybe a poem", "Or a song about fear"))


testFormat = "My name is {} {} bitch"
print(testFormat.format("Rick", "James"))
