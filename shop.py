class Shop:
    def __init__(self,name,price,qval):
        self.name=name
        self.price=price
        self.qval=qval
    def cost(self):
       return self.price * self.qval
    def inf(self):
        print(f'ГРУППА ТОВАРОВ  {self.name} ЦЕНА {self.price} КОЛИЧЕСТВО  {self.qval}')

class food( Shop):
    def __init__(self, name, price, qval,categ):
        self.name=name
        self.price=price
        self.qval=qval
        self.categ=categ 
    def info(self):
        print(f'НАЗВАНИЕ ПРОДУКТА {self.name} КАТЕГОРИЯ {self.categ} ЦЕНА {self.price}')
class house (Shop):
    def __init__ (self, name, price, qval, categ):
        self.name = name
        self.price = price
        self.qval = qval 
        self.categ= categ
    def info(self):
        print(f'НАЗВАНИЕ ПРОДУКТА {self.name} КАТЕГОРИЯ {self.categ} СТОИМОСТЬ {self.price}')
class prikol (Shop):
    def __init__ (self, name, price, qval, categ):
        self.name = name
        self.price = price
        self.qval = qval 
        self.categ= categ
    def info(self):
        print(f'НАЗВАНИЕ ПРОДУКТА {self.name} КАТЕГОРИЯ {self.categ} СТОИМОСТЬ {self.price}')
class grup:
    def __init__(self):
        self.items=[]
    def add(self, produkt):
        self.items.append(produkt)
        print(f'добавили {produkt.name}')
    def cocost(self):
        i=0
        for produkt in self.items:
            i+=produkt.cost()
        print(f'общая сумма {i}')
    def show(self):
        for produkt in self.items:
            produkt.info()
        self.cocost()


apple = food ('Яблоко', 50, 10, 'Еда')
lamp = house('Лампочка', 100, 15, 'Для дома')
stick = prikol ('Наклейки', 150, 5 ,'Приколы')
mgroup= grup()
mgroup.add(apple)
mgroup.add(lamp)
mgroup.add(stick)
mgroup.show()
