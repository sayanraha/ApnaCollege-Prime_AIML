# Given a list of integers compute the average of all numbers in the list.

a = [10,15,20,25,30]

sum = 0
for val in a:
    sum += val

avg = sum / len(a)
print("Average of the list is = ",avg)
