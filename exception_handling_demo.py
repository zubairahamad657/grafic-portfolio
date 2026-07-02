n = int(input("enter a number "))
d = int(input("enter a divisor "))

try:
    print(n / d)

except ZeroDivisionError as e:
    print(e)
    print("bye bye")
    raise Exception(f"Custom Error: {e}")