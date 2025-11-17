'''
Evaluate and print the result of the following expression:

x = 10 + 3 * 2 ** 2

Based on what you learnt in the lecture explain why the output is what it is.

'''

x = 10 + 3 * 2 ** 2
print(x) # output is 22

'''
Reason : 

x = 10 + 3 * 2 ** 2 , here 2 ** 2 has high precedence
x = 10 + 3 * 4, here 3 * 4 has high precedence
x = 10 + 12  = 22 (ans)

'''