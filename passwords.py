import random
class password:
    def __init__(self):
        pass 
    def pas(self,text):
        if len(text)<10:
            print('небезопасный пароль')
            return False 
        low =False
        up = False
        spec= False
        for x in text: 
            if x.islower():
                low = True
            if x.isupper():
                up=True
            if x.isdigit():
                spec=True
        if low and up and spec:
            print(f'пароль {text} хороший:)')
        else:
            print(f'пароль {text} плохой:(')
        def gen(self,length=12):
            xx='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            while True:
                new_pass = ''.join(random.choice(xx) for _ in range (length))
                if self.pas(new_pass):
                    return new_pass
passw = password()
passw.pas('passworD123')
passw.pas('!!!')
passw.pas('Password123!!!')
