'''
Create a program that :
1. Opens a file "name.txt" in write mode
2. Write 5 names (one per line) entered by the user
3. Then open the same file in read mode and print all names

'''

with open("name.txt","w") as f:
    for i in range(5):
        name = input("Enter name : ")
        f.write(name + "\n")
    print(f)

with open("name.txt","r") as f:
    print("Names present in the file : ")
    for line in f:
        print(line.strip())