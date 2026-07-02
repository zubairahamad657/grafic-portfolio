class circle:
       def __init__(self,r):
                self.radius = r
       def area(self):
                return 3.14 * self.radius * self.radius
c1 = circle(5)
print(c1.radius)
print(c1.area())
