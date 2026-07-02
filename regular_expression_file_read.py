import re
from turtle import st 
p = '\\b[a-z]{8}\\b'
print (re.compile(p))
print ("After Compile")
file = 'C:\\Users\\user\\Desktop\\python_programming\\kaay.txt'
string = "hey my name is zubair Iam from lucknow"
with open (file , 'r') as x:
    text = x.read()
result = re.search (p, text )
print (result)
result = re.findall (p, text )
print (result)
#print (re.sub (p, "hii there", string )) 