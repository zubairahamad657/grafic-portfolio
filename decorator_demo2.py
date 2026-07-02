def decorator(prog):
    def wrapper(a,b):
        
        print ("function started")
        print ("function namr:",prog.__name__)
        print ("*"*12) 
        result = prog(a,b)
        print ("*"*12)
        print ("function ended")
       # print ("*"*12)
        return result
    return wrapper 


@decorator
def multiply(a,b):
        print ("hello world!")
        return a*b
print(multiply(2,22))
        