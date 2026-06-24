def divide_info(n):
    divisors = []
    dividends = []
    remainders = []
    quotients = []
    factors = []
    for i in range(1, n+1):
        divisors.append(i)
        dividends.append(n)
        remainders.append(n%i)
        quotients.append(n/i)
        if n%i ==0:
            factors.append(i)
    print(dividends)
    print(divisors)
    print(quotients)
    print(remainders)
    print(factors)

def gcd(n, m):
    nset = set(i for i in range(1, n+1) if n%i == 0)
    mset = set(i for i in range(1, m+1) if m%i == 0)
    return max(nset.intersection(mset))

def gcd_euclidean_algo(n, m):
    a, b = 0, 0
    a, b = (n, m) if n > m else (m, n)
    while a > 0:
        a2 = a
        a = b
        b = a2%b
        if b == 0:
            break
    return a

print(gcd(31,13))
print(gcd_euclidean_algo(13,31))