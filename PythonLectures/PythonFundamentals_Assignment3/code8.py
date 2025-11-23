# Write a program to check whether two lists share no common elements.

# list1 = [1,2,3,4]
# list2 = [5,6,7,8]

list1 = [1,2,3]
list2 = [3,4]

s1 = set(list1)
s2 = set(list2)

check = s1.intersection(s2)
if len(check) < 1:
    print("No common element exist")
else :
    print("Common element exist")
print(s1)
print(s2)