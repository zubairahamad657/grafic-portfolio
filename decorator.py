def decorator(prog):
    def wrapper():
        print ("program stated") 
        prog()
        print ("program ended")
        return wrapper 
    @decorator
    def hey ():
        print ("program pending  ")

        hey()
        