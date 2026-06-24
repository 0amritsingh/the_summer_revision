def group_by_lenght(word):
    dic = {}
    for i in set(map(lambda x:len(x), word)):
        dic.update({i:[j for j in word if len(j) == i]})
    return dic

sentence = ['hi','bye','cat','to','dog','hello','he']
print(group_by_lenght(sentence))