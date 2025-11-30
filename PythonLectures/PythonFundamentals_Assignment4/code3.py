# Create a class Student with private attributes _name, _roll_no, and _marks.Provide getter  and  setter methods with validation (e.g., marks cannot be negative, roll number has to be between 1 & 100 & name cannot be empty).


class Student :
    def __init__(self,name,roll,marks):
        self.__name = name
        self.__roll = roll 
        self.__marks = marks
    
    def get_student_details(self):
        return  self.__name,self.__roll,self.__marks

    def set_student_details(self, name, roll, marks):
        
        if name == "":
            print("Name cannot be empty")
        if roll < 1 or roll > 100:
            print("Roll number has to be between 1 and 100")
        if marks < 0:
            print("Marks cannot be negative")
        else :
            self.__name = name
            self.__roll = roll
            self.__marks = marks


        

std = Student("Sumit",14,78)
print(std.get_student_details())
std.set_student_details("",0,-3)
std.set_student_details("Varun",16,87)
print(std.get_student_details())


