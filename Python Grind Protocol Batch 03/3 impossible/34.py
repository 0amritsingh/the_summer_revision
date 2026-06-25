x = 5
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
    inner()
    print(x)
outer()
print(x)

# OUPUT:
11
5
# explainition: so 'nonlocal is like global but only for the nearest nested/enclosing function' in this case for inner() the nearest enclosing function is outer() so the changes in x insider the inner() are also applied to outer()'s x but is nonlocal is yet not powerful enough to change the x outside both of the loops 