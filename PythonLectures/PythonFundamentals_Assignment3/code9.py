# Given a list, print all elements that appear more than once in the list.

list1 = [1,2,1,4,2,1,2,1]
res = {}

for num in list1:
    res[num] = res.get(num,0) + 1

for key,value in res.items():
    if(value > 1):
            print(f"Element {key} appear {value} times ")

