d = {}
for i in range(5):
    word = input(f'Enter word {i + 1}: ')
    d.update({i:word})
l = list(d.values())
print(l)