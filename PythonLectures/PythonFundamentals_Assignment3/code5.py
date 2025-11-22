'''
Create a dictionary where:

Keys = student names, Values = marks (integer)

Write a menu-based program where user presses a key ('A','B','C','D') depending on the operation they want to perform on the dictionary:
1. A - Add a student

2. B - Update marks

3. C - Search for a student

4. D - Display all students and marks

'''

n = int(input("Enter number of students you want : "))

student = {}

for _ in range(n):
    name = input("Enter name : ")
    marks = int(input(f"Enter marks for {name} : "))

    student[name] = marks

while True:
    choice = input("Enter any key among A,B,C and D for certain operations : ")
    match choice:

        case 'A':
            name = input("Enter name : ")
            marks = int(input(f"Enter marks for {name} : "))
            student[name] = marks
            print("Student added successfully.")
        case 'B':
            name = input("Enter the student name whose marks you want to update : ")
            marks = input("Enter the updated marks")
            student[name] = marks
            print(f"{name} marks updated successfully.")
        case 'C':
            name = input("Enter name to be searched")
            if(student.get(name) != None):
                print(f"Student {name} exist.")
            else:
                print(f"Student {name} do not exist.")
        case 'D':
            print("All students with their marks is : ", student)
        case _ :
            print("Wrong key enterd.")
            print("Program ended.")
            break
            