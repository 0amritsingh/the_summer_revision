a = [1,2,3]
b = [1,2,3]
c = a
# so, 'is' compare the exact location of object in the memory thats why the immutable like int, tuple always return True and mutable like list return False
# on the other hand, '==' compre the object itself thats why it return Ture if its exaclty matching the compared object 
print(a == b) # TRUE: objecticaly its matched exaclty
print(a is b) # FALSE: becuase a and b are list and lists are immutable
print(a is c) # TRUE: because c = a means c doesn't creats a new memory it IS same memory location of a