class Shape:
    def draw(self):
        print("Drawing a shape")

class Rectangle(Shape):  # Inherit from Shape
    def draw(self):
        print("Drawing a rectangle")

class Square(Shape):  # Inherit from Shape
    def draw(self):
        print("Drawing a square")  # Fixed the typo here

r = Rectangle()
r.draw()

s = Square()
s.draw()
