def flatten(l):
    f = []
    for i in l:
        if type(i) != list:
            f.append(i)
        else:
            for j in i:
                f.append(j)
    return f

lst = [1, [2,3], 4, [5,6]]
print(flatten(lst))

#NOTE: this only works for 2D to 1D that the quetion said (one level deep only) also the example they gave was also a 2D to 1D 