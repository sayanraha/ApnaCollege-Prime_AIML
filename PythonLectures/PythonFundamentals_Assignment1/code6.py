# Write a program to swap values of two numbers entered by the user.

n1 = float(input("Enter the 1st num : "))
n2 = float(input("Enter the 2nd num : "))

print('First number is : ',n1)
print('Second number is : ',n2)

# swap operations without using 3rd variable
n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2

print('First number is : ',n1)
print('Second number is : ',n2)