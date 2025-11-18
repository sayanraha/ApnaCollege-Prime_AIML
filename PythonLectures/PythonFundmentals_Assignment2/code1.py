
# ------------------------------------------------------------------------------
# Q1. Tax Calculation Program
# Write a program that takes salary as input. Using conditional statements,
# calculate the final tax rate based on these rules:
# - If salary <= 30,000 -> 5%
# - If salary > 30,000 to 70,000 -> 15%
# - If salary > 70,000 -> 25%
# ------------------------------------------------------------------------------


salary = float(input("Enter your salary : "))

if (salary <= 30000):
    print("Tax rate is = 5% ")
elif salary > 30000 and salary < 70000:
    print("Tax rate is = 15% ")
elif salary > 70000:
    print("Tax rate is = 25% ")
else :
    print("Wrong input entered.")