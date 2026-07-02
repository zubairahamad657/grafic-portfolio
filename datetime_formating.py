from datetime import datetime

now = datetime.now()

print(now.time())
print (now.strftime("%H:%M:%S"))#formatting time in 24 hour format
print(now.day)
print(now.month)
print(now.year)
print (now.strftime("%d/%m/%Y"))#formatting date in dd/mm/yyyy format
