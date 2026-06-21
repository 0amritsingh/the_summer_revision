d = {}
for i in range(5):
    word = input(f'Enter word {i + 1}: ')
    d.update({i:word})
for i in set(d.values()):
    print(f'{i}: {list(d.values()).count(i)}')
