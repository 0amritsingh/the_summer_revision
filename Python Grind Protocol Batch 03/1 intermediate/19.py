x = "hello"
y = "hello"
z = "".join(["h","e","l","l","o"])
print(x == y, x is y) # t, t
print(x == z, x is z) # t, f
# as i said before in 10.py that '==' checks the actull object and 'is' checks the memory location 