class acountMinus (Exception):
    def __init__(self, m,b):
        self.money = m
        self.balance = b
    def __str__(self):
        return f"money: {self.money}, balance: {self.balance}"
amount = int(input("Enter your amount :  "))
#balance = int(input("Enter your balance :  "))
try:
    if amount <= 100:
        print("you can withdraw")

    else:
        print("your account in minus")
        raise acountMinus(100, amount)
except acountMinus as x:
    print (x)
        
   
        