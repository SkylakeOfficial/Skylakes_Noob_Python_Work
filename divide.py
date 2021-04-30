def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

'''
这是递归的思路，但是做出来会自动缺省重复因数，不对
def div(n, lst):
    for i in range(2, n):
        if n % i == 0:
            if isprime(i) or i == 2:
                lst.append(i)
            else:
                lst.extend(div(i, []))
            n /= i
    return lst
'''
'''
你妈的，这个也不对头，炸了
def div(n):
    primes = []
    lst = []
    j = 0
    for i in range(2, n):
        if isprime(i):
            primes.append(i)
    while not isprime(n):
        if n % primes[j] == 0:
            n //= primes[j]
            lst.append(primes[j])
            
        else:
            j += 1
    return lst


我他妈直接抄一个
'''


def div(n):
    rlist = [1]
    i = 2

    while i <= n:
        if n % i == 0:
            rlist.append(i)
            n = n // i
            i = 2
            continue
        i += 1

    return rlist[1:]

n = int(input())


print(div(n))