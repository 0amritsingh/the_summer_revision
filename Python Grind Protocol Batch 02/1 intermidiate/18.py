langs = ['python','java','c++','rust','go']
new_langs = [i.upper() for i in langs if len(i) > 3]
print(new_langs)