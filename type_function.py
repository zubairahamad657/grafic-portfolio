data = input("enter anything: ")

print("Original Value =", data)
print("Original Type =", type(data))

num = int(data)
print("Int =", num)
print("Type =", type(num))

decimal = float(data)
print("Float =", decimal)
print("Type =", type(decimal))

text = str(num)
print("String =", text)
print("Type =", type(text))

value = bool(num)
print("Boolean =", value)
print("Type =", type(value))