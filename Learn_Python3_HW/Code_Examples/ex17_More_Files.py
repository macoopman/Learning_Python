from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two one one line, how?

# create in_file object from "from_file"
in_file = open(from_file) # think this might be a pointer to the file

indata = in_file.read() # and this is the actual data that we can use

#--- Extra and done need
# displays the side of indata
# print(f"The input file is {len(indata)} bytes long")
#
# # using the os library exist check that the file has been created
# print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()


# Opening the to_file with the 'w' so new file is created if does not exists
# else the file is erased
out_file = open(to_file, 'w')
# writing the data over
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
