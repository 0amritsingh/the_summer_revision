# B
a = [1, 2, 3]
b = a
b.append(4)
print(a)
# b = a does NOT copy. Both point to the same list. Use a.copy() to aboid this