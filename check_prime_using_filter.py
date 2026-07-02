def isPrime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(isPrime, lst)))