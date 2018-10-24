from sys import argv

script, num = argv


def factorial(num):
    if int(num) <= 1:
        return 1
    return int(num) * factorial(int(num) - 1)

print(f"Factorial of {num} = {factorial(num)}\n\n")
