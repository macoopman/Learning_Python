

#using input(), by default returns a string. So these inputs "numbers" are simply strings

print("How old are you?", end = " ")
age = input()

print("How tall are you?", end = " ")
height = input()

print("How much do you weight?", end = " ")
weight = int(input())  #this is how you would bring in a integer






print(f"So, you're {age} old, {height} tall and {weight} heavy")

# just practicing using both ways
print("So, you're {} old, {} tall and {} heavy".format(age,height,weight))
