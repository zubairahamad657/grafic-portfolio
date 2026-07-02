def fibonacci(n):
    a = 1
    b = 1

    for i in range(n):
        a, b = b, a + b
        yield a
#generator function to generate fibonacci numbers
x = fibonacci(8)
for num in x:
    print(num)
