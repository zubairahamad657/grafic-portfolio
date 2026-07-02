import re
from turtle import st 
p = '\\b[a-z]{3}\\b'
#print (re.compile(p))
#print ("After Compile")
string = "hey my name is zubair Iam from lucknow"
result = re.search (p, string )
print (result)
result = re.findall (p, string )
print (result)
print (re.sub (p, "hii there", string )) 