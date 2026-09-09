from math import sqrt, degrees, acos
class Vectors:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    def summ(self, xx, yy, zz):
        new_x=self.x+xx
        new_y=self.y+yy
        new_z=self.z+zz
        print(f'координата x {new_x} координата y {new_y} координата z {new_z}')
    def minus(self, xx, yy, zz):
        new_x=self.x-xx
        new_y=self.y-yy
        new_z=self.z-zz
        print(f'координата x {new_x} координата y {new_y} координата z {new_z}')
    def skal(self, xx,yy,zz):
        skalpr=self.x*xx+self.y*yy+self.z*zz
        print(f"скалярное произведение {skalpr}")
    def long(self):
        lon=sqrt(self.x**2+self.y**2+self.z**2)
        print(f"длина вектора {lon}")
    def angle(self,xx,yy,zz):
        skalpr=self.x*xx+self.y*yy+self.z*zz
        len1=sqrt(self.x**2+self.y**2+self.z**2)
        len2=sqrt(xx**2+yy**2+zz**2)
        if len1!=0 and len2!=0:
            cosa=skalpr/(len1*len2)
            if cosa>1:
                cosa=1
            if cosa<-1:
                cosa=-1
            angd=degrees(acos(cosa))
            print(f'угол {angd}')
        

vec=Vectors(1,2,3)
vec.summ(5,6,7)
vec.minus(1,5,9)
vec.skal(4,3,1)
vec.long()
vec.angle(4,1,7)
