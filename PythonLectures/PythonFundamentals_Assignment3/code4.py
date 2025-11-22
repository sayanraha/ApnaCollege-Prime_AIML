'''
Given a tuple of integers, create:
- A tuple of all even numbers
- A tuple of all odd numbers

'''

nums = (12,14,23,31,28,87,99,76,82)

even_nums = []
odd_nums = []

for i in nums :
    if i % 2 == 0:
        even_nums.append(i)
    else:
        odd_nums.append(i)

even_tuples = tuple(even_nums)
odd_tuples = tuple(odd_nums)
print("Even tuple is = ",even_tuples)
print("Odd tuple is = ",odd_tuples)