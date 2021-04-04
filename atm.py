class Atm(object):
    def _init_(self,pin,number,ammount):
        self.pin = pin
        self.number = number
        self.ammount = ammount
    
    def withdraw(self):
        print("withdrawn")
    def deposit(self):
        print("deposited")
    def change(self,new_ammount):
        self.ammount=new_ammount
        print(self.ammount)
    def balance(self):
        print(self.ammount)
    
no1=Atm("1","7293","82147929",500000)
no2=Atm("2","1023","74712772",820000)

print(no1.balance())
print(no2.balance())