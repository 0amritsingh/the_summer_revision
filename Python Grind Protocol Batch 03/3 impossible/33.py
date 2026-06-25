sen = 'hey how are you amrit singh nice to meet you'

# lst = list(filter(lambda x:x, [i for i in sen.split(' ') if len(i) > 3]))

lst = list(filter(lambda x: len(x) > 3, sen.split(' ')))
print(lst)