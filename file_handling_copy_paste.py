oldpath = 'C:\\Users\\user\\Desktop\\python_programming\\xx.txt'
newpath = 'C:\\Users\\user\\Desktop\\python_programming\\yy.txt'
try:
    with open (oldpath, 'r') as f:
        data = f.read ()
    with open (newpath, 'w') as g:
        g.write(data) 
        print ("file copied successfully")
except FileNotFoundError as x:
    print (x)           