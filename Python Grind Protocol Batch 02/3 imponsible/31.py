l = [5,2,8,1,9,3]
# m = []
# count = 0
# for i in l:
#     for j in l:
#         if i > j:
#             count += 1
#     m.append(count)
#     count = 0
m = [len([j for j in l if i > j]) for i in l]











print(m)

