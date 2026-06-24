l = [1,2,3,4,5,6,7,8,9,10]

# in a single line, map and filter chained together

print(list(map(lambda y:y**2,filter(lambda x:x%2==0, l))))