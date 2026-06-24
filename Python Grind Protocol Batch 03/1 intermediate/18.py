def count_vowels(s):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in vowels:
        count += s.count(i)
    return count

print(count_vowels('Amrit'))
print(count_vowels('Aakash'))
print(count_vowels('qwrt'))