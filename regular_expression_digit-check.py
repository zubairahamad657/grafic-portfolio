import re
#p = '\\b[a-z]{3}\\b'
p = '\\d{2}'
print (re.compile(p))
print ("After Compile")
string = "hey my house number is 44 577 56 356 "
result = re.search (p, string )
print (result)
result = re.findall (p, string )
print (result)
#print (re.sub (p, "hii there", string )) 