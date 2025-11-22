'''
Student enrollement : 

Given a list of tuples with info(name,subject):
    1. List all unique course
    2. List student enrolled in English
    3. create dictionary (student, set of courses)

'''

info = [
   ("Alice","Math"),
   ("Bob","Science"),
   ("Alice","Science"),
   ("Charlie","Math"),
   ("Bob","Math"),
   ("Alice","English"),
   ("Charlie","English")
]

courses = [] # declaring a course list for storing all the courses
s = set() # declaring an empty set to store unique courses
student = [] 
student_dict = {}

# for name,course in info :
#     if course == "English":
#         student.append(name)
#     s.add(course)

# print(s)
# print(student)


for name,course in info :

    if(student_dict.get(name) == None):
        student_dict.update({
            name : set()
        })
        student_dict[name].add(course)


print(student_dict)