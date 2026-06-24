def is_prime(n):
    if n == 2:
        return True
    else:
        for i in range(2, n):
            if n%i == 0:
                return False
        else:
            return True
            
for i in range(2, 51):
    if is_prime(i) == True:
        print(i, end=', ')
