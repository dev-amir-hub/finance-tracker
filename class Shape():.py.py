import math
class Shape():
    def area(self):
        print('площадь не определена')
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print(f'Площадь квадрата: {self.side**2} ')
class Ractangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        print(f'площадь прямоугольника : {self.width * self.height}')
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f'площадь круга : {self.radius**2 * math.pi}')
shapes=[Square(4),Ractangle(3,5),Circle(7)]
for shape in shapes:
    shape.area()

