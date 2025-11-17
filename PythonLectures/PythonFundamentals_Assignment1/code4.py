'''
The user enters a string containing a number(eg.,"45"). Convert it to : 
-> an integer
-> a float
-> a string again

Print all three values with their type.
'''

value = input("Enter the value : ")

value = int(value)
print(type(value), value)

value = float(value)
print(type(value),value)

value = str(value) # str() - converts anything to string
print(type(value),value)