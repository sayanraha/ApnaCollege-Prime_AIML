# WAF to print factorial of n
# 5! = 120 ,  5*4*3*2*1 = 120

# factorial using recursion
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

n = int(input('Enter the value of n :'))
ans = fact(n)

print("Factorial of ",n,"is",ans)





