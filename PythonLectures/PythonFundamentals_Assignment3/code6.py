'''
Given a list of words:

words=["apple","banana","kiwi","cherry","mango"]
Create a dictionary that maps each word to its length.
Example:
{"apple": 5, "banana": 6, "kiwi": 4, ...}

'''

words=["apple","banana","kiwi","cherry","mango"]

words_dict = {}
for w in words:
    words_dict[w] = len(w)

print("Dictionary is : ",words_dict)