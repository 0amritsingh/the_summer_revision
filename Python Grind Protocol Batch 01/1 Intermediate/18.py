name = 'Abdul Kalam'
if name.count(" ") == 1: 
    print(name[0], name[name.find(" ") + 1])
elif name.count(" ") == 2:
    print(name[0], name[name.find(" ") + 1], name[name.index(" ") + 1:][name.find(" ") + 1])
else:
    # i can make for 4 initials but not now
    pass