'''
print using if, elif ,else
 age < 13 - child
 age 13 - 18 - teenager
 age 18+ adult
'''

age = int(input("Enter age : "))

if age >= 0 and age < 13 :
    print("Child")
elif age >= 13 and age <= 18 :
    print("Teenager")
elif age > 18 :
    print("Adult")
else :
    print("Wrong input.....")