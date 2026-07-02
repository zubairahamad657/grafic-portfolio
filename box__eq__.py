class box:
     def __init__(self, l , w ,h):
        self.lenght = l
        self.width = w
        self.height = h
     def __eq__(self, box2):   
        return self.lenght == box2.lenght  and self.width == box2.width and self.height == box2.height
     

     
box1 = box(5, 5, 5)
box2 = box(5, 5, 5)
print(box1 == box2)
