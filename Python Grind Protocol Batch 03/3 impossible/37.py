def process(data):
    lst = list(map(lambda s:len(s), list(filter(lambda s:len(s)> 4, data))))
    #it says convet the remaining ones to uppercase and returns a list of their lenghts 
    # c'mon there is no reason to convert those remaining string to upper if you want thier lenths at this end

    return lst

lst = ['hey', 'amrit', 'gangster', 'brad', 'pitt', 'hollywood', ' ']
print(process(lst))

# no loops and no list comprehensions inside the loop