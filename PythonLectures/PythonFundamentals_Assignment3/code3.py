# Input two lists of integers from the user. Merge them into one list and sort the result.

list1 = [1,2,7]
list2 = [2,4,5]


for value in list2:
    list1.append(value)

print(list1)
list1.sort()
print("Final sorted merge list result is : ",list1)