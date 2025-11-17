'''
Take a decimal number as input (like 45.78) and output its:

integer part → 45
fractional part → .78

'''

num = float(input("Enter a decimal number = "))

integerPart = int(num)
FractionalPart = float(num - integerPart)

print('Integer part is : ',integerPart)
print('Fractional part is : ', FractionalPart)