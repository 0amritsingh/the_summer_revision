n = 1234
m = 0
while n > 0:
    l = n%10
    m = m*10 + l
    n = n//10
print(m)