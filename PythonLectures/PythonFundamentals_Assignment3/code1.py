# Check whether a string is palindrome or not.

str = input("Enter a string : ")

str1 = str[::-1] # stores reveres of the string

if str == str1:
    print("Palindrome string")
else :
    print("Not a Palindrome string")