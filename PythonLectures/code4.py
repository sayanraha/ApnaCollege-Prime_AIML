'''
Print vowels count in a word
eg. artificial intellignece
vowels = 10
'''

count = 0

word = "artificial intelligence"

for ch in word:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'): # vowel check condition
        count += 1

print('total vowels are = ',count)
