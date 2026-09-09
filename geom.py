import math

class figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx , dy):
        self.x+=dx
        self.y+=dy
        print(f'фигура теперь в точке {self.x} {self.y}')
class circle(figure):
    def __init__(self, x, y, radius):
        super().__init__(x,y)
        self.radius=radius
    def change(self, new_radius):
        old_radius=self.radius
        self.radius=new_radius
        print(f'старый радиус {old_radius} новый радиус {self.radius}')
    def square(self):
        msquare= (self.radius)**2 * math.pi
        print(f'площадь круга {msquare}')
class rectangle(figure):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w=w
        self.h=h 
    def change(self, nw, nh):
        self.w=nw
        self.h=nh
        print(f'новый размер прямоугольника{nw} на {nh}')
    def square(self):
        new_s=self.w*self.h
        print(f'площадь прямоугольника {new_s}')
class kwdr(figure):
    def __init__ (self, x, y, s):
        super().__init__(x,y)
        self.s=s
    def change(self, ns):
        self.s=ns
        print(f'квадрат новый размер {ns} на {ns}')
    def square(self):
        sq=self.s**2
        print(f'площадь квадрата{sq}')

circle1=circle(5, 8, 3)
circle1.change(4)
circle1.move(1,3)
circle1.square()
rectangle1=rectangle(1, 4, 5, 6)
rectangle1.change(3,2)
rectangle1.square()
rectangle1.move (8,9)
kwdr1=kwdr(8,3,5)
kwdr1.change(9)
kwdr1.move(2,8)
kwdr1.square()