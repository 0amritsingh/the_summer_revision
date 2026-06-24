def is_even(n):
    return True if n%2 == 0 else False
l = [1,2,3,4,5,6,7,8,9,10]
for i in l:
    if is_even(i) == True:
        print(i)
