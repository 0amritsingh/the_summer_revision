# only while loop, no string conversion , no sclicing

n = 12321
n2 = n
m = 0
while n > 0:
    l = n%10
    m = m*10 + l
    n = n//10
print(n == n2)