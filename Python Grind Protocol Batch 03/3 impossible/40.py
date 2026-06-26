def bubble_sort(lst):
    for i in lst:
        for i in range(len(lst) - 1):
            index = i
            bubble = lst[index]
            if lst[index] > lst[index + 1]:
                lst.remove(bubble)
                lst.insert(index + 1, bubble)
            else:
                index += 1
        lst = lst 
    return lst

l = [10,9,11,6,15,2]
print('Sorted list:', bubble_sort(l))

reverse = lambda l: bubble_sort(l)[::-1]
print('Reverse sorted list:', reverse(l))

only_even = list(filter(lambda e: e%2 ==0, bubble_sort(l)))
print('Only even numbers:', only_even)

even_square = list(map(lambda s:s**2, only_even))
print('Square of even numbers:', even_square)
