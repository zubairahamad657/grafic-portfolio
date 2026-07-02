def decorator(prog):
    def wrapper():
        print ("function started")
        print ("*"*12) 
        prog()
        print ("*"*12)
        print ("function ended")
       # print ("*"*12)
    return wrapper 
@decorator
def hey():
        print ("hello world!")
hey()
        