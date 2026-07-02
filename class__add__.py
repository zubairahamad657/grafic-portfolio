class box:
     def __init__(self, l , w ,h):
        self.lenght = l
        self.width = w
        self.height = h
     def __add__(self , box2):
         return box(self.lenght + box2.lenght , self.width + box2.width , self.height + box2.height)
box1 = box(1,2,3)
box2 = box(4,5,6)
box3 = box1 + box2
print(box3.lenght, box3.width, box3.height)        