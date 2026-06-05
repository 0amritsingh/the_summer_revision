# assuming the name only have first and last name there is no middle name or 
name = '    amrit     singh    '
a = name.strip()
f = a[:a.find(' ')]
l = a[a.find(' '):].strip()
print(f'\'{l.capitalize()}, {f.capitalize()}\'')