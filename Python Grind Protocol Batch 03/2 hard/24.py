x = 10
def foo():
    x = 20
    print(x)
foo()
print(x)

# explainaion: the above code will return 
20
10
# because x outside the function is 10 the line 6 will print that and x = 20 is inside the loop and then there is a print statement that will print the 20 
# so basicly the x outside is globle it can't use inside the funcion and x inside the function is local (for foo()) so it can't use outside 
# but there is a way that we can use the inner x as globle:
x = 10
def foo():
    global x
    x = 20
    print(x)
foo()
print(x)
# now the output will be 
20
20
# because at line 16 the inside x become globle and can be use outside and line 14 x = 10 came before the line 17 x = 20 that way the print statement at line 20 will print the x as 20
