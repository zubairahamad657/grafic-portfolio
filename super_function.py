class A:
    def __init__(self, n):
        self.name = n
class B(A): 
    def __init__(self, n, a):
        super ().__init__(n)
        self.age = a

    def display(self):
                print(f'Name: {self.name}, Age:{self.age}')
x = B("alicia",18)
x.display()
               

