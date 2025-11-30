'''
Create the following classes : Herbivore, Carnivore, Omnivore with some attributes & methods. Then create a class Bear that inherits from all the above classes to showcase how multiple inheritance works.
'''

class Herbivore:

    def __init__(self):
        self.dietH = "Only plants"

class Carnivore:
     def __init__(self):
        self.dietC = "Only animals"

class Omnivore:
     def __init__(self):
        self.dietO = "Both plants and animals"


class Bear (Herbivore,Carnivore,Omnivore):
    def __init__(self):
        super().__init__()
        Carnivore.__init__(self)
        Omnivore.__init__(self)
    
    def display_diet(self):
        print(f"Bear eats {self.dietH}, {self.dietC} and {self.dietO}")


obj = Bear()
obj.display_diet()