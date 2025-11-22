# WAF to return the count of digits of a number n.

def count_digits(n):

    count = 0
    while n != 0:
        d = int(n%10)
        if d > 0:
            count += 1
        n = int(n/10)
    print("Total digits count is = ",count)

n = int(input("Enter a number : "))
count_digits(n)