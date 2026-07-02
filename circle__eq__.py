class circle:
    def __init__(self, r):
        self.radius = r
    def __eq__(self, c2):
        return self.radius == c2.radius
c1 = circle (7)
c2 = circle (9)
print (c1 == c2)        