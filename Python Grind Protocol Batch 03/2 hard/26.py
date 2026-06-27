
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
        print(s)
        return 
    digit_sum(n , s)
    
digit_sum(1234) # 10
digit_sum(8989) # 34
digit_sum(10) # 1
digit_sum(2020) # 4