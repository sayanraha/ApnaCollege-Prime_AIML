# Write a function that takes two integers a and  b and prints all even numbers between them (inclusive).

def print_even(a,b):

    for i in range(a+1,b):
        if (i%2==0):
            print(i," is a even number") 
    return

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

print_even(a,b)