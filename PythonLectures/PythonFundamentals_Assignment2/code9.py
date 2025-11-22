# Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.

def is_prime(n):
    
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
   
    return True

n = int(input("Enter a number : "))

if (is_prime(n) == True):
    print("Prime number")
else:
    print("Not a prime number")