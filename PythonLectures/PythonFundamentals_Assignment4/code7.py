'''
Create a class Person that allows the constructor to work with:
-> name only
-> name + age
-> name + age + address

As direct constructor overloading (multiple constructors) are not allowed but we have to use default parameters to simulate constructor overloading.

'''

class Person:
    def __init__(self, name, age = None, address = None):
        self.name = name
        self.age = age
        self.address = address

    def get_Info(self):
        print(f"Name is : {self.name}")

        if self.age is not None :
            print(f"Age is : {self.age} years")

        if self.address is not None :
            print(f"Address is : {self.address} ")
        return

obj = Person("Sumit")
obj.get_Info()

obj1 = Person("Rahul",23)
obj1.get_Info()

obj2 = Person("Arun",25,"1,Rani Rash moni Bagan")
obj2.get_Info()

