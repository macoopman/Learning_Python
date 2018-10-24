## Program read in a command line arg indicating the number of trips taken
# Each trip records the milage and gallons of gas used
# output: mile/gallons for each trip and for the overall total

from sys import argv
from sys import exit

script = argv[0]
trips = 0
gallons = 0
miles = 0
totalGallons = 0
totalMiles = 0

# if no trip total is give. exit program 
if len(argv) != 2:
    print("Invalid Inputs")
    exit(0)
else:
    trips = argv[1]

# loop for given number of trips
for i in range(0,int(trips)):
    print(f"Trip {i + 1}: ")
    print("Enter gallons used: ", end = ' ')
    gallons = float(input())
    totalGallons += gallons

    print("Enter miles driven: ", end = ' ')
    miles = float(input())
    totalMiles += miles
    print(f"The miles / gallons for this tank was {(miles / gallons):.2f}")


print(f"\n\nThe overall average miles/gallons was {(totalMiles/totalGallons):.2f}")
