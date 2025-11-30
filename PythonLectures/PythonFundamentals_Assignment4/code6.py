# Create an abstract class Employee with an abstract method calculate_salary(). Create subclass Intern, FullTimeEmployee, and ContractEmployee that implement the method differently.


from abc import ABC,abstractmethod

# Abstract class
class Employee(ABC):
    @abstractmethod
    def calculate_salary():
        pass

class Intern(Employee):
    def __init__(self,basic,rent,allowences):
        self.basic = basic
        self.rent = rent
        self.allowences = allowences

    def calculate_salary(self):
        return self.basic + self.rent + self.allowences

class FullTimeEmployee(Employee):
    def __init__(self,basic,hra,da):
        self.basic = basic
        self.hra = hra
        self.da = da

    def calculate_salary(self):
        return self.basic + self.hra + self.da

class ContractEmployee(Employee):
    def __init__(self,hourly_rate,total_hours):
        self.hourly_rate = hourly_rate
        self.total_hours = total_hours

    def calculate_salary(self):
        return self.hourly_rate * self.total_hours


obj1 = Intern(15000,10000,8000)
print(f"Intern salary is = {obj1.calculate_salary()}/- ")

obj2 = FullTimeEmployee(25000,15000,12000)
print(f"Full time employee salary is = {obj2.calculate_salary()}/- ")

obj3 = ContractEmployee(750,180)
print(f"Contract employee salary is = {obj3.calculate_salary()}/- ")



