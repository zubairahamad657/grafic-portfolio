class date:
      def __init__(self,d,m,y):
            self.day = d
            self.month = m
            self.year = y

today = date (9, "jun", 2026 )   
print(today.day)
print(today.month)
print(today.year)
print("---------")      
tomorrow = date (10, "jun", 2026 )   
print(tomorrow.day)
print(tomorrow.month)
print(tomorrow.year)      