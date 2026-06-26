# def avg(l):
#     return sum(l)/len(l)
# print(avg([1,2,3]))


# def add(n):
#     if n == 0:
#         return 0
#     return add(n-1) + n
# print(add(10))


# def items(lst, idx = 0):
#     if idx == len(lst):
#         return
#     print(lst[idx])
#     items(lst, idx+1)
# items([1,2,3,4])


# def fact(n):
#     if n == 0:
#         return 1
#     return fact(n-1) * n
# print(fact(5))


a = 0
b = 1
for i in range(12):
    a, b = b, a + b

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144





def fab(n):
    if n == 0:
        return 0
    elif n == 1: 
        return 1
    else: 
        return fab(n-2) + fab(n-1)

for i in range(11):
    print(fab(i), end=', ')

  