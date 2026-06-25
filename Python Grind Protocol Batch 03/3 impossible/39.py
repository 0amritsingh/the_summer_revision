def is_perfect(n):
    a = sum([i for i in range(1, n) if n%i==0])
    return a

for i in range(1, 1001): 
    if i == is_perfect(i):
        print(i)
