word = ['apple', 'ant', 'banana', 'avocado', 'cherry', 'apricot']
new_word = list(filter(lambda a:a[0] == 'a', word))
print(new_word)