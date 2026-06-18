l = []
for i in range(5):
    word = input('Enter word: ')
    l.append(word.title())
v = [a for a in l if a[0] in ['A', 'E', 'I', 'O', 'U']]
c = [a for a in l if a[0] not in ['A', 'E', 'I', 'O', 'U']]
print(f'vowel list: {v}\nconsonant list: {c}')