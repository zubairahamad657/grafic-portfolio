class rectangle:
    def __init__(self, l,w):
        self.lenght = l
        self.width = w
    def __eq__(self, rect2):    
        return self.lenght == rect2.lenght and self.width == rect2.width
    
rect1 = rectangle(5, 10)
rect2 = rectangle(5, 7)
print(rect1 == rect2)