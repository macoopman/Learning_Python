from sys import argv

script, userInput = argv


def palindrome(pal):
    j = len(userInput) - 1
    isPalindrome = True

    # loop from left to right
    for i in range(0,len(userInput)):
            # compare index of input
            if(userInput[i] != userInput[j]):
                return False

            if(i == j and isPalindrome == True):
                return isPalindrome

            j -= 1




if palindrome(userInput):
    print(f"{userInput} is a palindrome\n\n")
else:
    print(f"{userInput} is not a palindrome\n\n")
