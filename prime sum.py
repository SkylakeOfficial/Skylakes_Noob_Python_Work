def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


def f(n):
    sm = 0
    t = 0
    for i in range(n, 2, -1):
        if t < 10 and isprime(i):
            sm += i
            t += 1
    return sm


p = int(input())
print(f(p))
