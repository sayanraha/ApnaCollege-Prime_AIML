# Write a function that prints a digit of a number,n.
# For example, n = 312, there are 3 digits in it 3,1,2 & we need to print them.

def print_digit(n):
 
    while n != 0 :
        d  = int(n % 10)
        print("Digit is = ",d)
        n = int(n / 10)
        
    return

n = int(input("Enter a number : "))
print_digit(n)