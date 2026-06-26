
n = 12345
s = 0
while n > 0:
    s += n%10
    n = n//10
# print(s)




# def digit_sum(n, s= 1):
#     if n == 0:
#         return 
#     digit_sum(n//10, s+n%10)
#     print(s)
#     return s
    


# digit_sum(12345)
# print(digit_sum(12345))


def digit_sum(n, s = 0): 
    s = s + n%10
    n = n//10
    if n==0:
        return s
    digit_sum(n , s)
    

digit_sum(1234)
print(digit_sum(1234))