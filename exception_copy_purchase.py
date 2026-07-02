class copyPrice (Exception):
    def __init__(self, p):
        self.price = p
    def __str__(self):
        return f"Price: {self.price}"
m = int(input("Enter price of the copy:  "))
try:
    if m >= 199:
        print("you can purchase")

    else:
        print("you cannot purchase")
        raise copyPrice (199)
except copyPrice as x:
    print (x)
        
   
        