'''
Create a base class Vehical with attributes like brand and model.
Create two subclasses Car and Bike that add extra attributes - seat(in Car) & engine_cc(in Bike).

'''

class Vehicle :
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model

class Car (Vehicle):
    def __init__(self,brand,model,seat):
        super().__init__(brand,model)
        self.seat = seat

class Bike (Vehicle):
    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc = engine_cc
    

# Creating objects

car = Car("Hyundai","XT-100","7seater")
print(f"Car features are Brand :{car.brand}, Model : {car.model}, Seat : {car.seat}")

bike = Bike("Yamaha","R15","500cc")
print(f"Bike features are Brand : {bike.brand}, Model : {bike.model}, Engine : {bike.engine_cc} ")


