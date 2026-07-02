class box:
     def __init__(self, l , w ,h):
        self.lenght = l
        self.width = w
        self.height = h
     def __contains__(self, item):
         if item == self.lenght or item == self.width or item == self.height:
             return True
         else:
             return False
box1 = box(2, 3, 4)
print(2 in box1)        