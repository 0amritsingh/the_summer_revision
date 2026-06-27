# without using sum(), loops, or any built in function
def sum_of_list(lst, sum = 0):
    if len(lst) == 0:
        print(sum)
        return 
    last = lst.pop()
    sum_of_list(lst, sum+last)

sum_of_list([1,2,3,4])