def table (num):
    for x in range (1, 11):
        print (num*x)
def sum (a,b):
     return a+b       

class student :
        def __init__(self,n, a):
            self.name = n 
            self.age = a
        def display (self):
            print (f'name:{self.name} age:{self.age}')    
class teacher:
     
    def __init__(self, n, s):
        self.name = n
        self.subject = s
    def display (self):
        print (f'name:{self.name} subject:{self.subject}')            