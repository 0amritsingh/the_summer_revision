# without  using slicing or built in reverse method
# that means we can use loops
def reverse_str(s, i=0):
    l = [j for j in s]
    last = l.pop()
    l.insert(i, last)
    s = ''.join(l)
    if i == len(l):
        print(s)
        return
    reverse_str(s, i + 1)
    
reverse_str('amrit') # tirma
reverse_str('harsh') # hsrah
reverse_str('nitin') # nitin (its a plaindrome)
