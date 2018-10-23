

def fun1(start, end, step):
    list = []
    i = start;
    print(">> Before Loop: Start = ", start, " : End = ", end)
    while i < end:
        print(">> In Loop: i = ", i)
        list.append(i)
        i += step

    return list


i = 0

#create an empty list
# numbers = []
#
# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)
#
#     i += 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")
#
#
# print("The numbers: ")
# for num in numbers:
#     print(num)


# testing out function verion
numbers2 = fun1(0,100,5)
print("The numbers2: ")
for num in numbers2:
    print(num)
