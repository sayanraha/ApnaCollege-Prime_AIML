# WAF to return sum of digits of a number

def sum_of_digits(n):
    sum = 0

    while n != 0:
        d = int(n%10)
        sum += d
        n = int(n/10)
    print('Sum of digits is = ',sum)
    return

n = int(input("Enter a number : "))
sum_of_digits(n)