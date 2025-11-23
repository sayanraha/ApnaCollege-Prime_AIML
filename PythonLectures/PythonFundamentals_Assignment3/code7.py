# Write a program that takes a string from the user and prints the number of spaces in the string.

str = input("Enter a string : ")
spaces = 0
for ch in str:
    if ch == ' ' or ch == " ":
        spaces += 1
    else :
        continue

print("Total number of spaces in the string is = ",spaces)