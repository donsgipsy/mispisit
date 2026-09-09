from math import sqrt 



class Kvadr_ur:
    def __init__(self, a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.d=0
    def diskr(self):
        self.d=self.b**2-4*self.a * self.c
    def solution(self):
        self.diskr()
        if self.d<0:
            print( 'искриминант меньше 0, привычных решений не существует')
        else:
          x1=(-self.b+sqrt(self.d) / (2*self.a))
          x2=(-self.b-sqrt(self.d) / (2*self.a))
          print(x1,x2)

uravnenie = Kvadr_ur(1,4,-5)
uravnenie.solution()