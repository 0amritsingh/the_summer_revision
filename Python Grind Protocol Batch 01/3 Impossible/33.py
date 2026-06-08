sen = input("Enter a sentance: ")
# they said not to use .title() and .capilatize() method so i have to use the .upper() method only 
newsenlst = []
senlst = sen.split(' ')
for i in senlst:
    newsenlst.append((i[0].upper() + i[1:]))

newsen = " ".join(newsenlst)
print(newsen)
# this question was impossible to make without loops ig idk

# so alright i saw the soution but even claude not able to solve this its because you can't solve this without loops but it gave a solution in which you can do it for 3 words like name only 
# so ig fuck this shi what i did is the best 
