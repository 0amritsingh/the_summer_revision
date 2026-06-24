student = [{'name':'Ali','marks':88}, {'name':'Sara','marks':72}, {'name':'Raj','marks':95}]

l = list(map(lambda x: f'{x['name']}: {x['marks']}/100', student))
    
print(l)