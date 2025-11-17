# Take two numbers as input from the user and print their sum, difference, product, and quotient.

num1 = float(input("Enter 1st number : "))
num2 = float(input("Enter 2nd number : "))

add = num1 + num2
difference = num1 - num2 if num1 > num2 else num2 - num1 #considering for postive diff
product = num1 * num2
quotient = num1/num2

print("Sum is = ",add)
print("Difference is = ",difference)
print("Product is = ",product)
print("Quotient is = ",quotient)
