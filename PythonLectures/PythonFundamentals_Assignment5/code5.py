'''
Write a program that tries to open "data.txt" in read mode.If the file does not exist, catch the exception and print "File not found!".

'''

try:
    f = open("data.txt")
    f.read()
except FileNotFoundError:
    print("File not found !")

