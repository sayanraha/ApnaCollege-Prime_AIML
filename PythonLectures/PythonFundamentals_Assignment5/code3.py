'''
Create a program that:
1. Has a list of numbers: [5,10,15,20,25]
2. Uses a list comprehension to create a new list with only numbers greater than 15.
3. Print the new list.
'''

nums = [5,10,15,20,25]
new_num = [n for n in nums if n > 15]
print(new_num)