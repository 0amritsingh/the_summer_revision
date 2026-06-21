# b

a = [1,2,3]
b = a.copy()
b.append(4)
c = set(a) | set(b)
print(sorted(c))

