

# printing formatted strings

def inch_to_cent(inches):
    return inches * 2.54

def lbs_to_kilo(lbs):
    return lbs * 2.205

name = "Mike A. Coopman"
age = 35
height = 67 #inches
weight = 176
eyes = "Green"
teeth = "White"
hair = "Brown"

# Error note: there cannot be a space b/t f and " " --> f"" NOT f ""
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall")
print(f"He's {inch_to_cent(height)} centimeters tall")
print(f"He's {weight} pounds heavy")
print(f"He's {round(lbs_to_kilo(weight))} kilos heavy")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair")
print(f"His teeth are usally {teeth} depending on the coffee")

# this line is trickey, try to get it exactly right

total = age + height + weight

print(f"If I add {age}, {height}, and {weight} I get {total}")
