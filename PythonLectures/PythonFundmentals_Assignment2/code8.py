# Simple calculator

def calculator(a,b,operation):

    if operation == '+':
        print("Sum is = ", a+b)
    elif operation == '-':
        print("Diff is = ", a - b if a > b else b - a)
    elif operation == '*':
        print("Product is = ",a*b)
    elif operation == "/":
        print("Division is = ", a / b if a > b else b / a)
    else :
        print("Wrong operator")
    
    return

a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = input("Enter the operator : ")

calculator(a,b,c)