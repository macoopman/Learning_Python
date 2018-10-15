# Goad: Simplify the last ex as much as possible

from sys import argv

script, fromFile, toFile = argv

# Open the input file
in_file = open(fromFile)


# Open the output file
out_file = open(toFile, 'w')

# read the input file into the output file
out_file.write(in_file.read());
