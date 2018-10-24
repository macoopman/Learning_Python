from sys import argv
from sys import exit


def sum(list):
    results = 0
    if(list == None):
        return 0
    else:
        for i in list:
            results += int(i)
    return results







if len(argv) > 1:
    intList = []
    for i in argv[1:]:
        intList.append(i)
else:
    print("Invalid arguments. No numbers given")
    exit(0)


print(f"Sum = {sum(intList)}  \n\n")
