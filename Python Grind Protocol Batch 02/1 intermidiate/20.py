items = {}
for i in range(3):
    item = input(f"Enter item {i + 1}: ")
    price = int(input(f"price of {item}: "))
    items.update({item: price})
print(items)