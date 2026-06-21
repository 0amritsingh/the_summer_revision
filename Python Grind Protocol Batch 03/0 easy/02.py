count = 0
while True:
    num = int(input('> '))
    if num < 0:
        count += num
        break
    count += num
print(count)