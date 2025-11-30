# Create a class Shape with a method area(). Create subclasses Circle, Rectangle and Triangle that overide the area () method.

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self,r):
        return 3.142 * r * r
        
class Rectangle(Shape):
    def area(self,length,breadth):
        return length * breadth

class Triangle(Shape):
    def area(self,base, height):
        return (1/2) * base * height

sp = Shape()

sp1 = Circle()
print(f"Area of a circle is = {sp1.area(5.5)} unitSquare")
sp2 = Rectangle()
print(f"Area of a rectangle is = {sp2.area(10,5)} unitSquare")
sp3 = Triangle()
print(f"Area of a rectangle is = {sp3.area(20,10)} unitSquare")