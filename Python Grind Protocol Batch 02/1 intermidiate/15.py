a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
if 3 in a.intersection(b):
    print(True)
else:
    print(False)
