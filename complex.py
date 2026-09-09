class Complex:
    def __init__(self, real, img):
        self.real=real
        self.img=img 
    def pluss (self, other, another): 
        new_real=self.real+other
        new_img=self.img+another
        print(f"{new_real} +{new_img}i")
    def minus(self, other, another):
        up_new= self.real-other
        down_new=self.img-another
        print(f"{up_new} - {abs(down_new)}i")
    def times(self, other, another):  
        new_real = self.real * other - self.img * another
        new_img = self.real * another + self.img * other
    
        if new_img >= 0:
            print(f"{new_real} + {new_img}i")
        else:
            print(f"{new_real} - {abs(new_img)}i")

reshenie = Complex(1, 3)
reshenie.pluss(2,4)
reshenie.minus (5,6)
reshenie.times(3,0)