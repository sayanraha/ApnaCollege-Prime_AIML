'''
Ask the user for a string and print: 
• All unique characters
• The count of unique characters
'''

# str = input("Enter a string : ")
str = "ranreteaswr"
unique_dict = {}

for ch in str:
    unique_dict[ch] =  unique_dict.get(ch,0) + 1

count = 0
res = ""
for key,value in unique_dict.items():
    if(value == 1):
        res += key + ","
        count += 1
print("Unique characters are : ",res)
print("Count of unique characters is = ",count)