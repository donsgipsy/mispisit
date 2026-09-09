class Account:
    def __init__(self, surname, acc_num, perc, data, summa):
        self.surname = surname
        self.acc_num = acc_num
        self.perc=perc
        self.data = data 
        self.summa= summa
    def shyatie_summa (self, new_summa):
        if new_summa <= self.summa:
            self.summa -= new_summa
        print(f'снято {new_summa}, остаток {self.summa}')
    def change_owner(self, new_owner):
        previous_owner=self.surname
        self.surname= new_owner
        print(f'старый владелец {previous_owner}, новый владелец {new_owner} ')
    def add_money(self, up_summa):
        previous_summa=self.summa
        self.summa+=up_summa
        print(f"старая сумма {previous_summa}' сумма с пополнением {up_summa} итог {self.summa}")
    def procenty (self):
        olds=self.summa
        self.summa=self.summa+self.summa*(self.perc/100)
        print(f'сумма с процентами {self.summa}')
    def dollar(self, dolsum):
        print(f'баланс в долларах {self.summa//dolsum}')
customer = Account ('Baranov', 123, 3, 4, 15000)
customer.shyatie_summa(2000) 
customer.change_owner('Sidirov')
customer.add_money(1234567)
customer.procenty()
customer.dollar(70)